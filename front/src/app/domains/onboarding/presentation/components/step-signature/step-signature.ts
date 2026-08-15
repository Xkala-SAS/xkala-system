import { Component, EventEmitter, Output, inject } from '@angular/core';

import { UploadSignatureUseCase } from '../../../application/use-cases/upload-signature.use-case';

import { ToastService } from '../../../../../core/services/toast.service';

import { Router } from '@angular/router';

import { GetOnboardingStatusUseCase } from '../../../application/use-cases/get-onboarding-status.use-case';

@Component({
  selector: 'app-step-signature',

  standalone: true,

  imports: [],

  templateUrl: './step-signature.html',

  styleUrl: './step-signature.scss',
})
export class StepSignature {
  private uploadUseCase = inject(UploadSignatureUseCase);

  private router = inject(Router);

  private getStatusUseCase = inject(GetOnboardingStatusUseCase);

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
        this.toast.show('Firma subida correctamente', 'success');
        this.completed.emit();
        this.validateCompletion();
      },

      error: (error) => {
        this.toast.show('Error al subir la firma', 'error');
        console.error(error);
      },
    });
  }

  private validateCompletion(): void {
    this.getStatusUseCase.execute().subscribe({
      next: (response: any) => {
        const status = response.data.status;

        if (status === 'COMPLETED') {
          this.toast.show('Onboarding finalizado correctamente', 'success');

          setTimeout(() => {
            this.router.navigate(['/dashboard']);
          }, 1000);
        }
      },

      error: () => {
        this.toast.show('No fue posible validar el onboarding', 'error');
      },
    });
  }
}
