export interface UserContract {
  id: string;

  position_id: string;

  position_name: string;

  contract_type_id: string;

  contract_type_name: string;

  fecha_ingreso: string;

  remuneration_type: string;

  remuneration_value: number;

  estado_laboral: boolean;
}
