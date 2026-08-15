import { Injectable, inject } from '@angular/core';

import { HttpClient } from '@angular/common/http';

import { Observable } from 'rxjs';

import { API_CONFIG } from '../../../../core/config/api.config';

@Injectable({
  providedIn: 'root',
})
export class AuthHttpRepository {
  private http = inject(HttpClient);

  login(data: any): Observable<any> {
    return this.http.post(`${API_CONFIG.baseUrl}/auth/login`, data);
  }
}
