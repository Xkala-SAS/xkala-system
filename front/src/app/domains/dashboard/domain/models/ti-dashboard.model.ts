export interface TiDashboard {
  users: {
    total: number;
    active: number;
    inactive: number;
  };

  documents: {
    total: number;
    signatures: number;
  };

  security: {
    roles: number;
    permissions: number;
  };
}
