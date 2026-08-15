export interface ContactItemRequest {
  contact_type: string;
  contact_value: string;
  is_primary: boolean;
}

export interface ContactsRequest {
  contacts: ContactItemRequest[];
}
