export interface RolePermission {
  id: string;

  codigo: string;

  descripcion: string;
}

export interface RoleDetail {
  id: string;

  nombre: string;

  descripcion: string;

  permissions: RolePermission[];
}
