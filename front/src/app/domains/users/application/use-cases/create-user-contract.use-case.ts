import { Injectable, inject } from '@angular/core';

import { UsersHttpRepository } from '../../infrastructure/repositories/user-http.repository';

import { SaveUserContractRequest } from '../../domain/models/save-user-contract-request.model';

@Injectable({
  providedIn: 'root',
})
export class CreateUserContractUseCase {
  private repository = inject(UsersHttpRepository);

  execute(userId: string, data: SaveUserContractRequest) {
    return this.repository.createUserContract(userId, data);
  }
}
