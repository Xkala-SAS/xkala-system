import { Injectable, inject } from '@angular/core';

import { RoleHttpRepository } from '../../infrastructure/repositories/role-http.repository';

@Injectable({
  providedIn: 'root',
})
export class GetRolesUseCase {
  private repository = inject(RoleHttpRepository);

  execute() {
    return this.repository.getRoles();
  }
}
