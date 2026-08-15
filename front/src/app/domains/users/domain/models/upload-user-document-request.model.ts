export interface UploadUserDocumentRequest {
  userId: string;

  documentType: string;

  file: File;
}
