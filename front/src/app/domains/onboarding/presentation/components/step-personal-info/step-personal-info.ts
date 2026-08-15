import { Component, inject, output } from '@angular/core';

import { CommonModule } from '@angular/common';

import { FormsModule } from '@angular/forms';

import { ToastService } from '../../../../../core/services/toast.service';

import { SavePersonalInfoUseCase } from '../../../application/use-cases/save-personal-info.use-case';

@Component({
  selector: 'app-step-personal-info',

  standalone: true,

  imports: [CommonModule, FormsModule],

  templateUrl: './step-personal-info.html',

  styleUrl: './step-personal-info.scss',
})
export class StepPersonalInfo {
  private savePersonalInfoUseCase = inject(SavePersonalInfoUseCase);

  private toastService = inject(ToastService);

  completed = output<void>();

  loading = false;

  form = {
    primer_nombre: '',

    segundo_nombre: '',

    primer_apellido: '',

    segundo_apellido: '',

    fecha_nacimiento: '',

    email: '',

    password: '',

    confirmPassword: '',
  };

  save(): void {
    if (!this.isValid()) {
      return;
    }

    this.loading = true;

    this.savePersonalInfoUseCase
      .execute({
        primer_nombre: this.form.primer_nombre,

        segundo_nombre: this.form.segundo_nombre,

        primer_apellido: this.form.primer_apellido,

        segundo_apellido: this.form.segundo_apellido,

        fecha_nacimiento: this.form.fecha_nacimiento,

        email: this.form.email,

        password: this.form.password,
      })
      .subscribe({
        next: () => {
          this.toastService.show('Información personal guardada correctamente', 'success');
          this.loading = false;
          this.completed.emit();
        },

        error: (error) => {
          console.error(error);
          this.toastService.show(
            error?.error?.message ?? 'Error guardando la información',
            'error',
          );
          this.loading = false;
        },
      });
  }

  private isValid(): boolean {
    if (
      !this.form.primer_nombre ||
      !this.form.primer_apellido ||
      !this.form.fecha_nacimiento ||
      !this.form.email ||
      !this.form.password
    ) {
      this.toastService.show('Complete todos los campos.', 'warning');

      return false;
    }

    if (this.form.password !== this.form.confirmPassword) {
      this.toastService.show('Las contraseñas no coinciden.', 'warning');

      return false;
    }

    return true;
  }
}
