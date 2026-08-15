export interface SaveUserContractRequest {
  position_id: string;

  contract_type_id: string;

  fecha_ingreso: string;

  remuneration_type: string;

  remuneration_value: number;

  estado_laboral?: boolean;
}
