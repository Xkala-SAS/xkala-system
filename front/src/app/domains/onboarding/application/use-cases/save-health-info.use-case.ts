import { Injectable, inject } from '@angular/core';

import { OnboardingHttpRepository } from '../../infrastructure/repositories/onboarding-http.repository';

import { HealthInfoRequest } from '../../domain/models/health-info-request.model';

@Injectable({
  providedIn: 'root',
})
export class SaveHealthInfoUseCase {
  private repository = inject(OnboardingHttpRepository);

  execute(request: HealthInfoRequest) {
    return this.repository.saveHealthInfo(request);
  }
}
