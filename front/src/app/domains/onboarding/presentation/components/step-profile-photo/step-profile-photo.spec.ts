import { ComponentFixture, TestBed } from '@angular/core/testing';

import { StepProfilePhoto } from './step-profile-photo';

describe('StepProfilePhoto', () => {
  let component: StepProfilePhoto;
  let fixture: ComponentFixture<StepProfilePhoto>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [StepProfilePhoto]
    })
    .compileComponents();

    fixture = TestBed.createComponent(StepProfilePhoto);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
