import { Injectable, inject } from '@angular/core';

import { Observable } from 'rxjs';

import { UsersHttpRepository } from '../../infrastructure/repositories/user-http.repository';

@Injectable({
  providedIn: 'root',
})
export class UploadUserDocumentUseCase {
  private repository = inject(UsersHttpRepository);

  uploadDocument(userId: string, documentType: string, file: File): Observable<any> {
    return this.repository.uploadDocument(userId, documentType, file);
  }

  uploadSignature(userId: string, file: File): Observable<any> {
    return this.repository.uploadSignature(userId, file);
  }
}
