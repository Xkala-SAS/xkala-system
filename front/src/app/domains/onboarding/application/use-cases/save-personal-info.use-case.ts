import { Injectable, inject } from '@angular/core';

import { OnboardingHttpRepository } from '../../infrastructure/repositories/onboarding-http.repository';

import { SavePersonalInfoRequest } from '../../domain/models/save-personal-info-request.model';

@Injectable({
  providedIn: 'root',
})
export class SavePersonalInfoUseCase {
  private repository = inject(OnboardingHttpRepository);

  execute(data: SavePersonalInfoRequest) {
    return this.repository.savePersonalInfo(data);
  }
}
