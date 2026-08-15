import { Injectable, inject } from '@angular/core';

import { HttpClient } from '@angular/common/http';

import { Observable, map } from 'rxjs';

import { API_CONFIG } from '../../../../core/config/api.config';

import { Role } from '../../domain/models/role.model';

@Injectable({
  providedIn: 'root',
})
export class RolesHttpRepository {
  private http = inject(HttpClient);

  getAll(): Observable<Role[]> {
    return this.http.get<any>(`${API_CONFIG.baseUrl}/roles`).pipe(map((response) => response.data));
  }
}
