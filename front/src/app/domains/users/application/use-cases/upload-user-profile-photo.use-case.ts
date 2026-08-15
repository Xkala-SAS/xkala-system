import { Injectable, inject } from '@angular/core';

import { Observable } from 'rxjs';

import { UsersHttpRepository } from '../../infrastructure/repositories/user-http.repository';

@Injectable({
  providedIn: 'root',
})
export class UploadUserProfilePhotoUseCase {
  private repository = inject(UsersHttpRepository);

  execute(userId: string, file: File): Observable<any> {
    return this.repository.uploadProfilePhoto(userId, file);
  }
}
