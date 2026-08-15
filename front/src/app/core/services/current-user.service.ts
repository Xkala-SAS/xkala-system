import { Injectable, signal } from '@angular/core';
import { UserProfile } from '../../domains/users/domain/models/user-profile.model';

@Injectable({
  providedIn: 'root',
})
export class CurrentUserService {
  user = signal<UserProfile | null>(null);

  setUser(user: UserProfile): void {
    this.user.set(user);
  }

  clear(): void {
    this.user.set(null);
  }

  hasPermission(permission: string): boolean {
    return this.user()?.permissions?.includes(permission) ?? false;
  }
}
