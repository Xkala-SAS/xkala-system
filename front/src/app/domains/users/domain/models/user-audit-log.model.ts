export interface UserAuditLog {
  id: string;

  action: string;

  resource: string;

  description: string;

  status_code: number;

  created_at: string;

  ip_address: string;
}
