import { Injectable, inject } from '@angular/core';

import { Observable } from 'rxjs';

import { Role } from '../../domain/models/role.model';

import { RolesHttpRepository } from '../../infrastructure/repositories/roles-http.repository';

@Injectable({
  providedIn: 'root',
})
export class GetRolesUseCase {
  private repository = inject(RolesHttpRepository);

  execute(): Observable<Role[]> {
    return this.repository.getAll();
  }
}
