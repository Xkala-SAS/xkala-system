import { Injectable, inject } from '@angular/core';

import { OnboardingHttpRepository } from '../../infrastructure/repositories/onboarding-http.repository';

import { ContactsRequest } from '../../domain/models/contact-request.model';

@Injectable({
  providedIn: 'root',
})
export class SaveContactsUseCase {
  private repository = inject(OnboardingHttpRepository);

  execute(request: ContactsRequest) {
    return this.repository.saveContacts(request);
  }
}
