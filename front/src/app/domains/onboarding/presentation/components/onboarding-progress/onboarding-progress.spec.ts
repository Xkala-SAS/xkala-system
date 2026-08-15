import { ComponentFixture, TestBed } from '@angular/core/testing';

import { OnboardingProgress } from './onboarding-progress';

describe('OnboardingProgress', () => {
  let component: OnboardingProgress;
  let fixture: ComponentFixture<OnboardingProgress>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [OnboardingProgress]
    })
    .compileComponents();

    fixture = TestBed.createComponent(OnboardingProgress);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
