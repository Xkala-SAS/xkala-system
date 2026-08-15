import { Component, EventEmitter, Output, inject } from '@angular/core';

import { CommonModule } from '@angular/common';

import { FormBuilder, ReactiveFormsModule, Validators } from '@angular/forms';

import { SaveContactsUseCase } from '../../../application/use-cases/save-contacts.use-case';

import { ToastService } from '../../../../../core/services/toast.service';

@Component({
  selector: 'app-step-contacts',

  standalone: true,

  imports: [CommonModule, ReactiveFormsModule],

  templateUrl: './step-contacts.html',

  styleUrl: './step-contacts.scss',
})
export class StepContacts {
  private fb = inject(FormBuilder);

  private saveContactsUseCase = inject(SaveContactsUseCase);

  private toast = inject(ToastService);

  @Output()
  completed = new EventEmitter<void>();

  form = this.fb.group({
    phone: ['', Validators.required],

    emergencyPhone: ['', Validators.required],
  });

  save(): void {
    if (this.form.invalid) {
      return;
    }

    const request = {
      contacts: [
        {
          contact_type: 'PHONE',
          contact_value: this.form.value.phone!,
          is_primary: true,
        },

        {
          contact_type: 'EMERGENCY_PHONE',
          contact_value: this.form.value.emergencyPhone!,
          is_primary: false,
        },
      ],
    };

    this.saveContactsUseCase.execute(request).subscribe({
      next: () => {
        this.toast.show('Contactos guardados correctamente', 'success');

        this.completed.emit();
      },

      error: (error) => {
        this.toast.show('Error al guardar los contactos', 'error');
        console.error(error);
      },
    });
  }
}
