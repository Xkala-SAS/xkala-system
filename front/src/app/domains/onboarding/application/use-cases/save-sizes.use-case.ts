import { Injectable, inject } from '@angular/core';

import { OnboardingHttpRepository } from '../../infrastructure/repositories/onboarding-http.repository';

import { SizeRequest } from '../../domain/models/size-request.model';

@Injectable({
  providedIn: 'root',
})
export class SaveSizesUseCase {
  private repository = inject(OnboardingHttpRepository);

  execute(request: SizeRequest) {
    return this.repository.saveSizes(request);
  }
}
