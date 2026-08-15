import { Injectable, inject } from '@angular/core';

import { Observable } from 'rxjs';

import { UsersHttpRepository } from '../../infrastructure/repositories/user-http.repository';

import { UserProfile } from '../../domain/models/user-profile.model';

@Injectable({
  providedIn: 'root',
})
export class GetUserProfileUseCase {
  private repository = inject(UsersHttpRepository);

  execute(userId: string): Observable<UserProfile> {
    return this.repository.getProfile(userId);
  }

  getMyProfile(): Observable<UserProfile> {
    return this.repository.getMyProfile();
  }
}
