import { Injectable, inject } from '@angular/core';

import { Observable } from 'rxjs';

import { UserDetail } from '../../domain/models/user-detail.model';

import { UsersHttpRepository } from '../../infrastructure/repositories/user-http.repository';

@Injectable({
  providedIn: 'root',
})
export class GetUserByIdUseCase {
  private repository = inject(UsersHttpRepository);

  execute(userId: string): Observable<UserDetail> {
    return this.repository.getById(userId);
  }
}
