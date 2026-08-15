import { Observable } from 'rxjs';

import { UserAuditLog } from '../models/user-audit-log.model';

export abstract class UserAuditLogRepository {
  abstract getByUserId(userId: string): Observable<UserAuditLog[]>;
}
