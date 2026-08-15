export interface UpdateUserRequest {
  primer_nombre: string;

  segundo_nombre?: string;

  primer_apellido: string;

  segundo_apellido?: string;

  email: string;

  role_id: string;

  estado: boolean;
}
