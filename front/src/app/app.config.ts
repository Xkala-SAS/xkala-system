import { ApplicationConfig } from '@angular/core';

import { provideBrowserGlobalErrorListeners } from '@angular/core';

import { provideRouter } from '@angular/router';

import { provideHttpClient, withInterceptors } from '@angular/common/http';

import { routes } from './app.routes';

import { authInterceptor } from './core/interceptors/auth.interceptor';

import { AUTH_REPOSITORY } from './domains/auth/domain/repositories/auth.repository';

import { AuthHttpRepository } from './domains/auth/infrastructure/repositories/auth-http.repository';

export const appConfig: ApplicationConfig = {
  providers: [
    provideBrowserGlobalErrorListeners(),

    provideRouter(routes),

    provideHttpClient(withInterceptors([authInterceptor])),

    {
      provide: AUTH_REPOSITORY,

      useClass: AuthHttpRepository,
    },
  ],
};
