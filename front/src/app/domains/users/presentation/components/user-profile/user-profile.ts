import { Component, OnInit, inject, input } from '@angular/core';

import { CommonModule, JsonPipe } from '@angular/common';

import { API_CONFIG } from '../../../../../core/config/api.config';

import { GetUserProfileUseCase } from '../../../application/use-cases/get-user-profile.use-case';

import { UploadUserProfilePhotoUseCase } from '../../../application/use-cases/upload-user-profile-photo.use-case';

import { UserDocuments } from '../user-documents/user-documents';

import { UserProfile as UserProfileModel } from '../../../domain/models/user-profile.model';

import { ToastService } from '../../../../../core/services/toast.service';

import { ImageUploadModal } from '../../../../../shared/ui/image-upload-modal/image-upload-modal';

import { UserAuditLogs } from '../user-audit-logs/user-audit-logs';

import { ContractModal } from '../contract-modal/contract-modal';

@Component({
  selector: 'app-user-profile',

  standalone: true,

  imports: [CommonModule, JsonPipe, UserDocuments, ImageUploadModal, UserAuditLogs, ContractModal],

  templateUrl: './user-profile.html',

  styleUrl: './user-profile.scss',
})
export class UserProfile implements OnInit {
  userId = input.required<string>();

  apiUrl = API_CONFIG.baseUrl;

  imageVersion = Date.now();

  private getUserProfileUseCase = inject(GetUserProfileUseCase);

  private uploadProfilePhotoUseCase = inject(UploadUserProfilePhotoUseCase);

  private toastService = inject(ToastService);

  profile: UserProfileModel | null = null;
  
  showContractModal = false;


  activeTab:
    | 'info'
    | 'documents'
    | 'files'
    | 'laboral'
    | 'afiliaciones'
    | 'direccion'
    | 'contactos'
    | 'audit' = 'info';

  loading = false;

  selectedPhoto: File | null = null;

  showPhotoModal = false;

  previewPhoto: string | null = null;



  ngOnInit(): void {
    this.loadProfile();
  }

  loadProfile(): void {
    this.loading = true;

    this.getUserProfileUseCase.execute(this.userId()).subscribe({
      next: (profile) => {
        this.profile = profile;

        this.imageVersion = Date.now();

        this.loading = false;
      },

      error: (error) => {
        console.error(error);

        this.loading = false;
      },
    });
  }

  viewSignature(): void {
    if (!this.profile?.signature) {
      return;
    }

    window.open(`${this.apiUrl}${this.profile.signature}`, '_blank');
  }

  openPhotoModal(): void {
    this.previewPhoto = this.profile?.profile_photo
      ? `${this.apiUrl}${this.profile.profile_photo}?v=${Date.now()}`
      : null;

    this.showPhotoModal = true;
  }

  closePhotoModal(): void {
    this.showPhotoModal = false;
  }

  onNewPhoto(file: File): void {
    this.selectedPhoto = file;

    const reader = new FileReader();

    reader.onload = () => {
      this.previewPhoto = reader.result as string;
    };

    reader.readAsDataURL(file);
  }

  onPhotoSelected(event: Event): void {
    const input = event.target as HTMLInputElement;

    if (input.files && input.files.length > 0) {
      this.selectedPhoto = input.files[0];

      this.uploadProfilePhoto();
    }
  }

  uploadProfilePhoto(): void {
    if (!this.selectedPhoto) {
      return;
    }

    this.uploadProfilePhotoUseCase.execute(this.userId(), this.selectedPhoto).subscribe({
      next: () => {
        this.toastService.show('Foto actualizada correctamente', 'success');

        this.closePhotoModal();

        this.loadProfile();
      },

      error: (error) => {
        this.toastService.show(error?.error?.message || 'Error subiendo foto', 'error');
      },
    });
  }

  openContractModal(): void {
    this.showContractModal = true;
  }

  closeContractModal(): void {
    this.showContractModal = false;
  }
}
