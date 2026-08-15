import { ComponentFixture, TestBed } from '@angular/core/testing';

import { StepSizes } from './step-sizes';

describe('StepSizes', () => {
  let component: StepSizes;
  let fixture: ComponentFixture<StepSizes>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [StepSizes]
    })
    .compileComponents();

    fixture = TestBed.createComponent(StepSizes);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
