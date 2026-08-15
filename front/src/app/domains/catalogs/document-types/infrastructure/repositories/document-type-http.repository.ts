import { Injectable, inject } from '@angular/core';

import { HttpClient } from '@angular/common/http';

import { Observable, map } from 'rxjs';

import { API_CONFIG } from '../../../../../core/config/api.config';

import { DocumentType } from '../../domain/models/document-type.model';

@Injectable({
  providedIn: 'root',
})
export class DocumentTypeHttpRepository {
  private http = inject(HttpClient);

  getAll(): Observable<DocumentType[]> {
    return this.http
      .get<any>(`${API_CONFIG.baseUrl}/document-types`)
      .pipe(map((response) => response.data));
  }
}
