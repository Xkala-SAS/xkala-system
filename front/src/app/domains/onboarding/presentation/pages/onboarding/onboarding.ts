import { Component } from '@angular/core';

import { StepAddress } from '../../components/step-address/step-address';

import { OnboardingProgress } from '../../components/onboarding-progress/onboarding-progress';

import { StepContacts } from '../../components/step-contacts/step-contacts';

import { StepHealth } from '../../components/step-health/step-health';

import { StepSizes } from '../../components/step-sizes/step-sizes';

import { StepProfilePhoto } from '../../components/step-profile-photo/step-profile-photo';

import { StepSignature } from '../../components/step-signature/step-signature';

import { StepPersonalInfo } from '../../components/step-personal-info/step-personal-info';

@Component({
  selector: 'app-onboarding',

  standalone: true,

  imports: [
    StepPersonalInfo,

    StepAddress,

    StepContacts,

    StepHealth,

    StepSizes,

    StepProfilePhoto,

    StepSignature,

    OnboardingProgress,
  ],

  templateUrl: './onboarding.html',

  styleUrl: './onboarding.scss',
})
export class Onboarding {
  currentStep = 1;

  totalSteps = 7;

  stepTitles = [
    'Información personal',
    'Dirección',

    'Contactos',

    'Afiliaciones',

    'Dotación',

    'Foto de perfil',

    'Firma',
  ];

  nextStep(): void {
    if (this.currentStep < this.totalSteps) {
      this.currentStep++;
    }
  }

  previousStep(): void {
    if (this.currentStep > 1) {
      this.currentStep--;
    }
  }
}
