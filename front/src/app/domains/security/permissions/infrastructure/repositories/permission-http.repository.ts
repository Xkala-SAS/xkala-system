import { Injectable, inject } from '@angular/core';

import { HttpClient } from '@angular/common/http';

import { Observable, map } from 'rxjs';

import { API_CONFIG } from '../../../../../core/config/api.config';

import { Permission } from '../../domain/models/permission.model';

@Injectable({
  providedIn: 'root',
})
export class PermissionHttpRepository {
  private http = inject(HttpClient);

  getAll(): Observable<Permission[]> {
    return this.http
      .get<any>(`${API_CONFIG.baseUrl}/permissions`)
      .pipe(map((response) => response.data));
  }
}
