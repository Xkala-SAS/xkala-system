import { Injectable, inject } from '@angular/core';

import { Observable } from 'rxjs';

import { UserDocument } from '../../domain/models/user-document.model';

import { UsersHttpRepository } from '../../infrastructure/repositories/user-http.repository';

@Injectable({
  providedIn: 'root',
})
export class GetUserDocumentsUseCase {
  private repository = inject(UsersHttpRepository);

  execute(userId: string): Observable<UserDocument[]> {
    return this.repository.getDocuments(userId);
  }
}
