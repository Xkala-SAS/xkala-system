import { Observable } from 'rxjs';

import { InjectionToken } from '@angular/core';

import { LoginRequest } from '../models/login-request.model';

import { LoginResponse } from '../models/login-response.model';

export interface AuthRepository {
  login(credentials: LoginRequest): Observable<LoginResponse>;
}

export const AUTH_REPOSITORY = new InjectionToken<AuthRepository>('AUTH_REPOSITORY');
