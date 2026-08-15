import { Injectable, inject } from '@angular/core';

import { Observable } from 'rxjs';

import { DocumentType } from '../../domain/models/document-type.model';

import { DocumentTypesHttpRepository } from '../../infrastructure/repositories/document-types-http.repository';

@Injectable({
  providedIn: 'root',
})
export class GetDocumentTypesUseCase {
  private repository = inject(DocumentTypesHttpRepository);

  execute(): Observable<DocumentType[]> {
    return this.repository.getAll();
  }
}
