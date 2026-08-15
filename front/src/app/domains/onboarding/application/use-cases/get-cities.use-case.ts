import { inject, Injectable } from '@angular/core';

import { OnboardingHttpRepository } from '../../infrastructure/repositories/onboarding-http.repository';

@Injectable({
  providedIn: 'root',
})
export class GetCitiesUseCase {
  private repository = inject(OnboardingHttpRepository);

  execute() {
    return this.repository.getCities();
  }
}
