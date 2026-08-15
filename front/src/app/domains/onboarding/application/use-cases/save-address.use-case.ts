import { Injectable, inject } from '@angular/core';

import { OnboardingHttpRepository } from '../../infrastructure/repositories/onboarding-http.repository';

import { AddressRequest } from '../../domain/models/address-request.model';

@Injectable({
  providedIn: 'root',
})
export class SaveAddressUseCase {
  private repository = inject(OnboardingHttpRepository);

  execute(request: AddressRequest) {
    return this.repository.saveAddress(request);
  }
}
