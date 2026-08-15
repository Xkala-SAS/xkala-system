import { Injectable, inject } from '@angular/core';

import { OnboardingHttpRepository } from '../../infrastructure/repositories/onboarding-http.repository';

@Injectable({
  providedIn: 'root',
})
export class UploadProfilePhotoUseCase {
  private repository = inject(OnboardingHttpRepository);

  execute(file: File) {
    return this.repository.uploadProfilePhoto(file);
  }
}
