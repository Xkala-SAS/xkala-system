import { Injectable, inject } from '@angular/core';

import { HttpClient } from '@angular/common/http';

import { Observable, map } from 'rxjs';

import { API_CONFIG } from '../../../../../core/config/api.config';

import { Role } from '../../domain/models/role.model';

import { RoleDetail } from '../../domain/models/role-detail.model';

@Injectable({
  providedIn: 'root',
})
export class RoleHttpRepository {
  private http = inject(HttpClient);

  getRoles(): Observable<Role[]> {
    return this.http.get<any>(`${API_CONFIG.baseUrl}/roles`).pipe(map((response) => response.data));
  }

  getRoleDetail(roleId: string): Observable<RoleDetail> {
    return this.http
      .get<any>(`${API_CONFIG.baseUrl}/roles/${roleId}`)
      .pipe(map((response) => response.data));
  }

  getRoleById(roleId: string) {
    return this.http
      .get<any>(`${API_CONFIG.baseUrl}/roles/${roleId}`)
      .pipe(map((response) => response.data as RoleDetail));
  }
}
