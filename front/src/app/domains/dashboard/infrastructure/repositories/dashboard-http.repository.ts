import { Injectable, inject } from '@angular/core';

import { HttpClient } from '@angular/common/http';

import { Observable, map } from 'rxjs';

import { API_CONFIG } from '../../../../core/config/api.config';

import { TiDashboard } from '../../domain/models/ti-dashboard.model';

@Injectable({
  providedIn: 'root',
})
export class DashboardHttpRepository {
  private http = inject(HttpClient);

  getTiDashboard(): Observable<TiDashboard> {
    return this.http
      .get<any>(`${API_CONFIG.baseUrl}/dashboard/ti`)
      .pipe(map((response) => response.data));
  }
}
