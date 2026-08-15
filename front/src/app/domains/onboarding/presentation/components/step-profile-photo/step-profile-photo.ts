import { Component, EventEmitter, Output, inject } from '@angular/core';

import { UploadProfilePhotoUseCase } from '../../../application/use-cases/upload-profile-photo.use-case';

import { ToastService } from '../../../../../core/services/toast.service';

@Component({
  selector: 'app-step-profile-photo',

  standalone: true,

  imports: [],

  templateUrl: './step-profile-photo.html',

  styleUrl: './step-profile-photo.scss',
})
export class StepProfilePhoto {
  private uploadUseCase = inject(UploadProfilePhotoUseCase);
  private toast = inject(ToastService);

  @Output()
  completed = new EventEmitter<void>();

  selectedFile?: File;

  onFileSelected(event: Event): void {
    const input = event.target as HTMLInputElement;

    if (!input.files?.length) {
      return;
    }

    this.selectedFile = input.files[0];
  }

  upload(): void {
    if (!this.selectedFile) {
      return;
    }

    this.uploadUseCase.execute(this.selectedFile).subscribe({
      next: () => {
        this.toast.show('Foto de perfil subida correctamente', 'success');
        this.completed.emit();
      },

      error: (error) => {
        this.toast.show('Error al subir la foto', 'error');
        console.error(error);
      },
    });
  }
}
