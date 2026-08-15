import { Component, computed, input } from '@angular/core';

@Component({
  selector: 'app-onboarding-progress',

  standalone: true,

  imports: [],

  templateUrl: './onboarding-progress.html',

  styleUrl: './onboarding-progress.scss',
})
export class OnboardingProgress {
  currentStep = input.required<number>();

  totalSteps = input.required<number>();

  percentage = computed(() => {
    return Math.round((this.currentStep() / this.totalSteps()) * 100);
  });
}
