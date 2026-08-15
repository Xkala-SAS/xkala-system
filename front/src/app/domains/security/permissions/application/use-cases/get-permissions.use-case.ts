import { Injectable, inject } from '@angular/core';

import { PermissionHttpRepository } from '../../infrastructure/repositories/permission-http.repository';

@Injectable({
  providedIn: 'root',
})
export class GetPermissionsUseCase {
  private repository = inject(PermissionHttpRepository);

  execute() {
    return this.repository.getAll();
  }
}
