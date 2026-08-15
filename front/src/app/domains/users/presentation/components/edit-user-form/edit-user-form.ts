import { Component, OnInit, inject, input, output } from '@angular/core';

import { CommonModule } from '@angular/common';

import { FormsModule } from '@angular/forms';

import { GetRolesUseCase } from '../../../../roles/application/use-cases/get-roles.use-case';

import { GetUserByIdUseCase } from '../../../application/use-cases/get-user-by-id.use-case';

import { UpdateUserUseCase } from '../../../application/use-cases/update-user.use-case';

import { ToastService } from '../../../../../core/services/toast.service';

import { Role } from '../../../../roles/domain/models/role.model';

@Component({
  selector: 'app-edit-user-form',

  standalone: true,

  imports: [CommonModule, FormsModule],

  templateUrl: './edit-user-form.html',

  styleUrl: './edit-user-form.scss',
})
export class EditUserForm implements OnInit {
  userId = input.required<string>();

  updated = output<void>();

  private getRolesUseCase = inject(GetRolesUseCase);

  private getUserByIdUseCase = inject(GetUserByIdUseCase);

  private updateUserUseCase = inject(UpdateUserUseCase);

  private toastService = inject(ToastService);

  roles: Role[] = [];

  loading = false;

  form = {
    primer_nombre: '',

    segundo_nombre: '',

    primer_apellido: '',

    segundo_apellido: '',

    email: '',

    role_id: '',

    estado: true,
  };

  ngOnInit(): void {
    this.loadRoles();

    this.loadUser();
  }

  loadRoles(): void {
    this.getRolesUseCase.execute().subscribe({
      next: (roles) => {
        this.roles = roles;
      },

      error: console.error,
    });
  }

  loadUser(): void {
    this.getUserByIdUseCase.execute(this.userId()).subscribe({
      next: (user) => {
        this.form = {
          primer_nombre: user.primer_nombre,

          segundo_nombre: user.segundo_nombre ?? '',

          primer_apellido: user.primer_apellido,

          segundo_apellido: user.segundo_apellido ?? '',

          email: user.email,

          role_id: user.role_id,

          estado: user.estado,
        };
      },

      error: console.error,
    });
  }

  save(): void {
    this.loading = true;

    this.updateUserUseCase.execute(this.userId(), this.form).subscribe({
      next: () => {
        this.toastService.show('Usuario actualizado correctamente', 'success');

        this.updated.emit();

        this.loading = false;
      },

      error: (error) => {
        console.error(error);

        this.toastService.show('Error actualizando usuario', 'error');

        this.loading = false;
      },
    });
  }
}
