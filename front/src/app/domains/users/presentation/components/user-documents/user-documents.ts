import { Component, OnInit, inject, input } from '@angular/core';

import { CommonModule } from '@angular/common';

import { FormsModule } from '@angular/forms';

import { ToastService } from '../../../../../core/services/toast.service';

import { ConfirmDialog } from '../../../../../shared/ui/confirm-dialog/confirm-dialog';

import { UserDocument } from '../../../domain/models/user-document.model';

import { GetUserDocumentsUseCase } from '../../../application/use-cases/get-user-documents.use-case';

import { UploadUserDocumentUseCase } from '../../../application/use-cases/upload-user-document.use-case';

import { DeleteUserDocumentUseCase } from '../../../application/use-cases/delete-user-document.use-case';

import { API_CONFIG } from '../../../../../core/config/api.config';

import { USER_FILE_TYPES } from '../../../domain/constants/user-file-types';

@Component({
  selector: 'app-user-documents',

  standalone: true,

  imports: [CommonModule, FormsModule, ConfirmDialog],

  templateUrl: './user-documents.html',

  styleUrl: './user-documents.scss',
})
export class UserDocuments implements OnInit {
  private getDocumentsUseCase = inject(GetUserDocumentsUseCase);

  private uploadDocumentUseCase = inject(UploadUserDocumentUseCase);

  private deleteDocumentUseCase = inject(DeleteUserDocumentUseCase);

  private toastService = inject(ToastService);

  apiUrl = API_CONFIG.baseUrl;

  userId = input.required<string>();

  documents: UserDocument[] = [];

  fileTypes = USER_FILE_TYPES;

  loading = false;

  selectedFile: File | null = null;

  fileType = '';

  showDeleteDialog = false;

  documentToDelete: UserDocument | null = null;

  ngOnInit(): void {
    this.loadDocuments();
  }

  loadDocuments(): void {
    this.loading = true;

    this.getDocumentsUseCase.execute(this.userId()).subscribe({
      next: (documents) => {
        this.documents = documents.filter((item) => item.file_type !== 'signature');

        this.loading = false;
      },

      error: (error) => {
        console.error(error);

        this.loading = false;
      },
    });
  }

  onFileSelected(event: Event): void {
    const input = event.target as HTMLInputElement;

    if (input.files && input.files.length > 0) {
      this.selectedFile = input.files[0];
    }
  }

  uploadDocument(): void {
    if (!this.selectedFile || !this.fileType) {
      this.toastService.show('Seleccione archivo y tipo', 'error');

      return;
    }

    const request =
      this.fileType === 'signature'
        ? this.uploadDocumentUseCase.uploadSignature(this.userId(), this.selectedFile)
        : this.uploadDocumentUseCase.uploadDocument(
            this.userId(),
            this.fileType,
            this.selectedFile,
          );

    request.subscribe({
      next: () => {
        this.toastService.show(
          this.fileType === 'signature'
            ? 'Firma cargada correctamente'
            : 'Archivo cargado correctamente',
          'success',
        );

        this.fileType = '';

        this.selectedFile = null;

        this.loadDocuments();
      },

      error: (error) => {
        console.error(error);

        this.toastService.show(error?.error?.message || 'Error cargando archivo', 'error');
      },
    });
  }

  getDocumentLabel(code: string): string {
    const documentType = this.fileTypes.find((item) => item.codigo === code);

    return documentType?.nombre || code;
  }

  viewDocument(document: UserDocument): void {
    window.open(`${this.apiUrl}${document.file_path}`, '_blank');
  }

  deleteDocument(document: UserDocument): void {
    this.documentToDelete = document;

    this.showDeleteDialog = true;
  }

  confirmDeleteDocument(): void {
    if (!this.documentToDelete) {
      return;
    }

    this.deleteDocumentUseCase.execute(this.documentToDelete.id).subscribe({
      next: () => {
        this.toastService.show('archivo eliminado correctamente', 'success');

        this.closeDeleteDialog();

        this.loadDocuments();
      },

      error: (error) => {
        console.error(error);

        this.toastService.show(error?.error?.message || 'Error eliminando archivo', 'error');
      },
    });
  }

  closeDeleteDialog(): void {
    this.showDeleteDialog = false;

    this.documentToDelete = null;
  }

  isImage(path: string): boolean {
    const extensions = ['jpg', 'jpeg', 'png', 'webp'];

    const extension = path.split('.').pop()?.toLowerCase();

    return !!extension && extensions.includes(extension);
  }
}
