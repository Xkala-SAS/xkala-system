import { Component, OnInit, inject, output } from '@angular/core';

import { CommonModule } from '@angular/common';

import { FormsModule } from '@angular/forms';

import { Role } from '../../../../roles/domain/models/role.model';

import { DocumentType } from '../../../../document-types/domain/models/document-type.model';

import { GetRolesUseCase } from '../../../../roles/application/use-cases/get-roles.use-case';

import { GetDocumentTypesUseCase } from '../../../../document-types/application/use-cases/get-document-types.use-case';

import { CreateUserUseCase } from '../../../application/use-cases/create-user.use-case';

import { ToastService } from '../../../../../core/services/toast.service';

@Component({
  selector: 'app-create-user-form',

  standalone: true,

  imports: [CommonModule, FormsModule],

  templateUrl: './create-user-form.html',

  styleUrl: './create-user-form.scss',
})
export class CreateUserForm implements OnInit {
  private getRolesUseCase = inject(GetRolesUseCase);

  private getDocumentTypesUseCase = inject(GetDocumentTypesUseCase);

  private createUserUseCase = inject(CreateUserUseCase);

  private toastService = inject(ToastService);

  roles: Role[] = [];

  documentTypes: DocumentType[] = [];

  loading = false;

  userCreated = output<void>();

  form = {
    numero_documento: '',

    document_type_id: '',

    role_id: '',
  };

  ngOnInit(): void {
    this.loadRoles();

    this.loadDocumentTypes();
  }

  loadRoles(): void {
    this.getRolesUseCase.execute().subscribe({
      next: (roles) => {
        this.roles = roles;
      },

      error: (error) => {
        console.error(error);
      },
    });
  }

  loadDocumentTypes(): void {
    this.getDocumentTypesUseCase.execute().subscribe({
      next: (documentTypes) => {
        this.documentTypes = documentTypes;
      },

      error: (error) => {
        console.error(error);
      },
    });
  }

  isFormValid(): boolean {
    return (
      !!this.form.numero_documento &&
      !!this.form.document_type_id &&
      !!this.form.role_id
    );
  }

  save(): void {
    if (!this.isFormValid()) {
      this.toastService.show(
        'Complete todos los campos obligatorios',
        'warning'
      );

      return;
    }

    this.loading = true;

    this.createUserUseCase.execute(this.form).subscribe({
      next: () => {
        this.toastService.show(
          'Usuario preregistrado correctamente',
          'success'
        );

        this.userCreated.emit();

        this.loading = false;

        this.form = {
          numero_documento: '',
          document_type_id: '',
          role_id: '',
        };
      },

      error: (error) => {
        console.error(error);

        this.toastService.show(
          error?.error?.message ?? 'Error creando usuario',
          'error'
        );

        this.loading = false;
      },
    });
  }
}