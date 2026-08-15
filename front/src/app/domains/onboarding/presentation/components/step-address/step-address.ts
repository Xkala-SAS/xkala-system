import { Component, EventEmitter, OnInit, Output, inject } from '@angular/core';

import { CommonModule } from '@angular/common';

import { FormBuilder, ReactiveFormsModule, Validators } from '@angular/forms';

import { City } from '../../../domain/models/city.model';

import { GetCitiesUseCase } from '../../../application/use-cases/get-cities.use-case';

import { SaveAddressUseCase } from '../../../application/use-cases/save-address.use-case';

import { ToastService } from '../../../../../core/services/toast.service';

@Component({
  selector: 'app-step-address',

  standalone: true,

  imports: [CommonModule, ReactiveFormsModule],

  templateUrl: './step-address.html',

  styleUrl: './step-address.scss',
})
export class StepAddress implements OnInit {
  private fb = inject(FormBuilder);

  private getCitiesUseCase = inject(GetCitiesUseCase);

  private saveAddressUseCase = inject(SaveAddressUseCase);

  private toast = inject(ToastService);

  cities: City[] = [];

  loading = false;

  form = this.fb.group({
    direccion: ['', Validators.required],

    barrio: ['', Validators.required],

    city_id: ['', Validators.required],
  });

  ngOnInit(): void {
    this.loadCities();
  }

  loadCities(): void {
    this.loading = true;

    this.getCitiesUseCase.execute().subscribe({
      next: (cities) => {
        this.cities = cities;

        this.loading = false;
      },

      error: () => {
        this.loading = false;
      },
    });
  }

  @Output()
  completed = new EventEmitter<void>();

  save(): void {
    if (this.form.invalid) {
      return;
    }

    this.saveAddressUseCase.execute(this.form.getRawValue() as any).subscribe({
      next: () => {
        this.toast.show('Direccion guardada correctamente', 'success');
        this.completed.emit();
      },

      error: (error) => {
        this.toast.show('Error al guardar direccion', 'error');
        console.error(error);
      },
    });
  }
}
