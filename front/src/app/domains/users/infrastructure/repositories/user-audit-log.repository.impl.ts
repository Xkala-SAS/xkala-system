import { Injectable, inject } from '@angular/core';

import { HttpClient } from '@angular/common/http';

import { Observable, map } from 'rxjs';

import { API_CONFIG } from '../../../../core/config/api.config';

import { UserAuditLog } from '../../domain/models/user-audit-log.model';

import { UserAuditLogRepository } from '../../domain/repositories/user-audit-log.repository';

@Injectable({
  providedIn: 'root',
})
export class UserAuditLogRepositoryImpl implements UserAuditLogRepository {
  private http = inject(HttpClient);

  getByUserId(userId: string): Observable<UserAuditLog[]> {
    return this.http
      .get<any>(`${API_CONFIG.baseUrl}/users/${userId}/audit-logs`)
      .pipe(map((response) => response.data));
  }
}
