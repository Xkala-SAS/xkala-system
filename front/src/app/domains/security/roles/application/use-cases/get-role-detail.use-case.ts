import { Injectable, inject } from '@angular/core';

import { RoleHttpRepository } from '../../infrastructure/repositories/role-http.repository';

@Injectable({
  providedIn: 'root',
})
export class GetRoleDetailUseCase {
  private repository = inject(RoleHttpRepository);

  execute(roleId: string) {
    return this.repository.getRoleById(roleId);
  }
}
