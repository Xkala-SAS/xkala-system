import { ComponentFixture, TestBed } from '@angular/core/testing';

import { StepSignature } from './step-signature';

describe('StepSignature', () => {
  let component: StepSignature;
  let fixture: ComponentFixture<StepSignature>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [StepSignature]
    })
    .compileComponents();

    fixture = TestBed.createComponent(StepSignature);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
