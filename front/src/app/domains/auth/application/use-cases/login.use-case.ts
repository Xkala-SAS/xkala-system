import { Injectable, inject } from '@angular/core';

import { Observable, tap } from 'rxjs';

import { LoginRequest } from '../../domain/models/login-request.model';

import { LoginResponse } from '../../domain/models/login-response.model';

import { AUTH_REPOSITORY } from '../../domain/repositories/auth.repository';

import { SessionService } from '../../infrastructure/services/session.service';

@Injectable({
  providedIn: 'root',
})
export class LoginUseCase {
  private repository = inject(AUTH_REPOSITORY);

  private sessionService = inject(SessionService);

  execute(credentials: LoginRequest): Observable<LoginResponse> {
    return this.repository.login(credentials).pipe(
      tap((response) => {
        this.sessionService.setAccessToken(response.data.access_token);
      }),
    );
  }
}
