import { Injectable, inject } from '@angular/core';

import { HttpClient } from '@angular/common/http';

import { Observable } from 'rxjs';

import { API_CONFIG } from '../../../../core/config/api.config';

import { ChangePasswordRequest } from '../../domain/models/change-password-request.model';

@Injectable({
  providedIn: 'root',
})
export class AccountHttpRepository {
  private http = inject(HttpClient);

  changePassword(data: ChangePasswordRequest): Observable<any> {
    return this.http.post(`${API_CONFIG.baseUrl}/users/change-password`, data);
  }
}
