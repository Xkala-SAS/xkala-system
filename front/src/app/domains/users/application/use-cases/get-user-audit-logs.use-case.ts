import { Injectable, inject } from '@angular/core';

import { Observable } from 'rxjs';

import { UserAuditLog } from '../../domain/models/user-audit-log.model';

import { UserAuditLogRepositoryImpl } from '../../infrastructure/repositories/user-audit-log.repository.impl';

@Injectable({
  providedIn: 'root',
})
export class GetUserAuditLogsUseCase {
  private repository = inject(UserAuditLogRepositoryImpl);

  execute(userId: string): Observable<UserAuditLog[]> {
    return this.repository.getByUserId(userId);
  }
}
