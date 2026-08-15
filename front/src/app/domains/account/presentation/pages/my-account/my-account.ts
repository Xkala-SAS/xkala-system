import { Component, inject } from '@angular/core';

import { CommonModule } from '@angular/common';

import { FormsModule } from '@angular/forms';

import { CurrentUserService } from '../../../../../core/services/current-user.service';

import { ChangePasswordUseCase } from '../../../application/use-cases/change-password.use-case';

@Component({
  selector: 'app-my-account',

  standalone: true,

  imports: [CommonModule, FormsModule],

  templateUrl: './my-account.html',

  styleUrl: './my-account.scss',
})
export class MyAccount {
  private currentUserService = inject(CurrentUserService);

  private changePasswordUseCase = inject(ChangePasswordUseCase);

  profile = this.currentUserService.user();

  currentPassword = '';

  newPassword = '';

  confirmPassword = '';

  loading = false;

  successMessage = '';

  errorMessage = '';

  changePassword(): void {
    this.successMessage = '';

    this.errorMessage = '';

    if (this.newPassword !== this.confirmPassword) {
      this.errorMessage = 'Las contraseñas no coinciden';

      return;
    }

    this.loading = true;

    this.changePasswordUseCase
      .execute({
        current_password: this.currentPassword,

        new_password: this.newPassword,
      })
      .subscribe({
        next: (response) => {
          this.successMessage = response.message;

          this.currentPassword = '';

          this.newPassword = '';

          this.confirmPassword = '';

          this.loading = false;
        },

        error: (error) => {
          this.errorMessage = error?.error?.message ?? 'Error al actualizar contraseña';

          this.loading = false;
        },
      });
  }
}
