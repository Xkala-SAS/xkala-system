import { Injectable, inject } from '@angular/core';

import { UsersHttpRepository } from '../../infrastructure/repositories/user-http.repository';

@Injectable({
  providedIn: 'root',
})
export class UploadUserSignatureUseCase {
  private repository = inject(UsersHttpRepository);

  execute(userId: string, file: File) {
    return this.repository.uploadSignature(userId, file);
  }
}
