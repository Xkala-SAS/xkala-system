import { Injectable, inject } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { map, Observable } from 'rxjs';

import { API_CONFIG } from '../../../../core/config/api.config';
import { CatalogItem } from '../../domain/models/catalog-item.model';

@Injectable({
  providedIn: 'root',
})
export class HrHttpRepository {
  private http = inject(HttpClient);

  getEps(): Observable<CatalogItem[]> {
    return this.http
      .get<any>(`${API_CONFIG.baseUrl}/hr/eps`)
      .pipe(map((response) => response.data));
  }

  getArls(): Observable<CatalogItem[]> {
    return this.http
      .get<any>(`${API_CONFIG.baseUrl}/hr/arls`)
      .pipe(map((response) => response.data));
  }

  getPensionFunds(): Observable<CatalogItem[]> {
    return this.http
      .get<any>(`${API_CONFIG.baseUrl}/hr/pension-funds`)
      .pipe(map((response) => response.data));
  }

  getSeveranceFunds(): Observable<CatalogItem[]> {
    return this.http
      .get<any>(`${API_CONFIG.baseUrl}/hr/severance-funds`)
      .pipe(map((response) => response.data));
  }

  getPositions(): Observable<any[]> {
    return this.http
      .get<any>(`${API_CONFIG.baseUrl}/hr/positions`)
      .pipe(map((response) => response.data));
  }

  getContractTypes(): Observable<CatalogItem[]> {
    return this.http
      .get<any>(`${API_CONFIG.baseUrl}/hr/contract-types`)
      .pipe(map((response) => response.data));
  }
}
