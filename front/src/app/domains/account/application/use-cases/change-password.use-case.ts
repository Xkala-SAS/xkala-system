import { Injectable, inject } from '@angular/core';

import { Observable } from 'rxjs';

import { AccountHttpRepository } from '../../infrastructure/repositories/account-http.repository';

import { ChangePasswordRequest } from '../../domain/models/change-password-request.model';

@Injectable({
  providedIn: 'root',
})
export class ChangePasswordUseCase {
  private repository = inject(AccountHttpRepository);

  execute(data: ChangePasswordRequest): Observable<any> {
    return this.repository.changePassword(data);
  }
}
