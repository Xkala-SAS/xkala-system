export interface SavePersonalInfoRequest {
  primer_nombre: string;

  segundo_nombre?: string;

  primer_apellido: string;

  segundo_apellido?: string;

  fecha_nacimiento: string;

  email: string;

  password: string;
}
