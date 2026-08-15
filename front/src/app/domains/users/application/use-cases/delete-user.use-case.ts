import { Injectable, inject } from '@angular/core';

import { Observable } from 'rxjs';

import { UsersHttpRepository } from '../../infrastructure/repositories/user-http.repository';

@Injectable({
  providedIn: 'root',
})
export class DeleteUserUseCase {
  private repository = inject(UsersHttpRepository);

  execute(userId: string): Observable<any> {
    return this.repository.deleteUser(userId);
  }
}
