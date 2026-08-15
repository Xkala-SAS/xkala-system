import { Injectable, inject } from '@angular/core';

import { Observable } from 'rxjs';

import { CreateUserRequest } from '../../domain/models/create-user-request.model';

import { UsersHttpRepository } from '../../infrastructure/repositories/user-http.repository';

@Injectable({
  providedIn: 'root',
})
export class CreateUserUseCase {
  private repository = inject(UsersHttpRepository);

  execute(data: CreateUserRequest): Observable<any> {
    return this.repository.createUser(data);
  }
}
