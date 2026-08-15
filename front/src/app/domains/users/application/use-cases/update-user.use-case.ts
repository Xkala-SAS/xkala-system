import { Injectable, inject } from '@angular/core';

import { Observable } from 'rxjs';

import { UsersHttpRepository } from '../../infrastructure/repositories/user-http.repository';

@Injectable({
  providedIn: 'root',
})
export class UpdateUserUseCase {
  private repository = inject(UsersHttpRepository);

  execute(userId: string, data: any): Observable<any> {
    return this.repository.updateUser(userId, data);
  }
}
