import { Component, EventEmitter, Output, inject } from '@angular/core';

import { CommonModule } from '@angular/common';

import { FormBuilder, ReactiveFormsModule, Validators } from '@angular/forms';

import { SaveSizesUseCase } from '../../../application/use-cases/save-sizes.use-case';

import { ToastService } from '../../../../../core/services/toast.service';

@Component({
  selector: 'app-step-sizes',

  standalone: true,

  imports: [CommonModule, ReactiveFormsModule],

  templateUrl: './step-sizes.html',

  styleUrl: './step-sizes.scss',
})
export class StepSizes {
  private fb = inject(FormBuilder);

  private saveSizesUseCase = inject(SaveSizesUseCase);

  private toast = inject(ToastService);

  @Output()
  completed = new EventEmitter<void>();

  form = this.fb.group({
    shirt_size: ['', Validators.required],

    pants_size: ['', Validators.required],

    shoe_size: ['', Validators.required],
  });

  save(): void {
    if (this.form.invalid) {
      return;
    }

    this.saveSizesUseCase.execute(this.form.getRawValue() as any).subscribe({
      next: () => {
        this.toast.show('Tallas guardadas correctamente', 'success');
        this.completed.emit();
      },

      error: (error) => {
        this.toast.show('Error al guardar las tallas', 'error');
        console.error(error);
      },
    });
  }
}
