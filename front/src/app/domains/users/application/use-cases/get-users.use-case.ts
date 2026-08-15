import { Injectable, inject } from '@angular/core';

import { Observable } from 'rxjs';

import { UsersResponse } from '../../domain/models/users-response.model';

import { UsersHttpRepository } from '../../infrastructure/repositories/user-http.repository';

@Injectable({
  providedIn: 'root',
})
export class GetUsersUseCase {
  private repository = inject(UsersHttpRepository);

  execute(
    page: number,
    limit: number,
    search: string = '',
    estado?: boolean,
    orderBy: string = 'created_at',
    direction: string = 'desc',
  ): Observable<UsersResponse> {
    return this.repository.getUsers(page, limit, search, estado, orderBy, direction);
  }
}
