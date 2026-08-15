import { Injectable, inject } from '@angular/core';

import { Observable } from 'rxjs';

import { DocumentType } from '../../domain/models/document-type.model';

import { CatalogHttpRepository } from '../../infrastructure/repositories/catalog-http.repository';

@Injectable({
  providedIn: 'root',
})
export class GetDocumentTypesUseCase {
  private repository = inject(CatalogHttpRepository);

  execute(): Observable<DocumentType[]> {
    return this.repository.getDocumentTypes();
  }
}
