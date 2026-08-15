import { Injectable, inject } from '@angular/core';

import { UsersHttpRepository } from '../../infrastructure/repositories/user-http.repository';

@Injectable({
  providedIn: 'root',
})
export class GetUserContractUseCase {
  private repository = inject(UsersHttpRepository);

  execute(userId: string) {
    return this.repository.getUserContract(userId);
  }
}
