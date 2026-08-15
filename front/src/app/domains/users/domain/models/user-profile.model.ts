export interface UserProfile {
  id: string;

  nombre_completo: string;

  profile_photo?: string;

  signature?: string;

  email: string;

  estado: boolean;

  rol: string;

  permissions?: string[];

  documento: any;

  direccion: any;

  contactos: any[];

  afiliaciones: any;

  laboral?: {
    cargo: string;
    tipo_contrato: string;
    fecha_ingreso: string;

    remuneration_type: string;

    remuneration_value: number;

    activo: boolean;
  };

  tallas: any;

  archivos: any[];
}
