import { Component, inject } from '@angular/core';

import { FormsModule } from '@angular/forms';

import { Router } from '@angular/router';

import { AuthHttpRepository } from '../../../infrastructure/repositories/auth-http.repository';

import { SessionService } from '../../../infrastructure/services/session.service';

import { GetOnboardingStatusUseCase } from '../../../../onboarding/application/use-cases/get-onboarding-status.use-case';

import { ToastService } from '../../../../../core/services/toast.service';

import { GetUserProfileUseCase } from '../../../../users/application/use-cases/get-user-profile.use-case';

import { CurrentUserService } from '../../../../../core/services/current-user.service';

@Component({
  selector: 'app-login',

  standalone: true,

  imports: [FormsModule],

  templateUrl: './login.html',

  styleUrl: './login.scss',
})
export class Login {
  private authRepository = inject(AuthHttpRepository);

  private sessionService = inject(SessionService);

  private router = inject(Router);

  private getOnboardingStatusUseCase = inject(GetOnboardingStatusUseCase);

  private toast = inject(ToastService);

  private getUserProfileUseCase = inject(GetUserProfileUseCase);

  private currentUserService = inject(CurrentUserService);

  numeroDocumento = '';

  password = '';

  loading = false;

  login() {
    this.loading = true;

    this.authRepository
      .login({
        numero_documento: this.numeroDocumento,

        password: this.password,
      })

      .subscribe({
        next: (response: any) => {
          this.sessionService.setAccessToken(response.data.access_token);

          this.getUserProfileUseCase.getMyProfile().subscribe({
            next: (profile) => {
              this.currentUserService.setUser(profile);

              this.getOnboardingStatusUseCase.execute().subscribe({
                next: (statusResponse: any) => {
                  const status = statusResponse.data.status;

                  if (status === 'PENDING') {
                    this.toast.show('Primer inicio de sesion, ¡completa tus datos!', 'success');

                    this.router.navigate(['/onboarding']);

                    return;
                  }

                  this.toast.show('Bienvenido a XKALA', 'success');

                  this.router.navigate(['/dashboard']);
                },
              });
            },
          });
        },

        error: (err) => {
          console.error(err);
          this.toast.show('Error en credenciales', 'error');

          this.loading = false;
        },
      });
  }
}
