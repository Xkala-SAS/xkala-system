import { Injectable, inject } from '@angular/core';

import { OnboardingHttpRepository } from '../../infrastructure/repositories/onboarding-http.repository';

@Injectable({
  providedIn: 'root',
})
export class GetOnboardingStatusUseCase {
  private repository = inject(OnboardingHttpRepository);

  execute() {
    return this.repository.getStatus();
  }
}
