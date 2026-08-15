import { Injectable, inject } from '@angular/core';

import { Observable } from 'rxjs';

import { DocumentType } from '../../domain/models/document-type.model';

import { DocumentTypeHttpRepository } from '../../infrastructure/repositories/document-type-http.repository';

@Injectable({
  providedIn: 'root',
})
export class GetDocumentTypesUseCase {
  private repository = inject(DocumentTypeHttpRepository);

  execute(): Observable<DocumentType[]> {
    return this.repository.getAll();
  }
}
