import { Component, OnInit, inject } from '@angular/core';
import { CommonModule } from '@angular/common';

import { GetUserProfileUseCase } from '../../../../users/application/use-cases/get-user-profile.use-case';
import { UserProfile } from '../../../../users/domain/models/user-profile.model';

import { API_CONFIG } from '../../../../../core/config/api.config';

@Component({
  selector: 'app-employee-home',

  standalone: true,

  imports: [CommonModule],

  templateUrl: './employee-home.html',

  styleUrl: './employee-home.scss',
})
export class EmployeeHome implements OnInit {
  private getUserProfileUseCase = inject(GetUserProfileUseCase);

  profile: UserProfile | null = null;

  apiUrl = API_CONFIG.baseUrl;

  ngOnInit(): void {
    this.loadProfile();
  }

  loadProfile(): void {
    this.getUserProfileUseCase.getMyProfile().subscribe({
      next: (profile) => {
        this.profile = profile;
      },
    });
  }

  get profilePhoto(): string | null {
    const file = this.profile?.archivos?.find((item) => item.tipo === 'profile_photo');

    return file ? this.apiUrl + file.ruta : null;
  }
}
