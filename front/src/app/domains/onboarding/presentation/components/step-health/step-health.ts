import { Component, OnInit, EventEmitter, Output, inject } from '@angular/core';

import { CommonModule } from '@angular/common';

import { FormBuilder, ReactiveFormsModule, Validators } from '@angular/forms';

import { SaveHealthInfoUseCase } from '../../../application/use-cases/save-health-info.use-case';

import { CatalogItem } from '../../../../hr/domain/models/catalog-item.model';

import { HrHttpRepository } from '../../../../hr/infrastructure/repositories/hr-http.repository';

import { ToastService } from '../../../../../core/services/toast.service';

@Component({
  selector: 'app-step-health',

  standalone: true,

  imports: [CommonModule, ReactiveFormsModule],

  templateUrl: './step-health.html',

  styleUrl: './step-health.scss',
})
export class StepHealth implements OnInit {
  private fb = inject(FormBuilder);

  private saveHealthInfoUseCase = inject(SaveHealthInfoUseCase);

  private hrRepository = inject(HrHttpRepository);

  private toast = inject(ToastService);

  eps: CatalogItem[] = [];

  arls: CatalogItem[] = [];

  pensionFunds: CatalogItem[] = [];

  severanceFunds: CatalogItem[] = [];

  ngOnInit(): void {
    this.loadCatalogs();
  }

  @Output()
  completed = new EventEmitter<void>();

  form = this.fb.group({
    eps_id: ['', Validators.required],

    arl_id: ['', Validators.required],

    pension_fund_id: ['', Validators.required],

    severance_fund_id: ['', Validators.required],
  });

  save(): void {
    if (this.form.invalid) {
      return;
    }

    this.saveHealthInfoUseCase.execute(this.form.getRawValue() as any).subscribe({
      next: () => {
        this.toast.show('Afiliaciones guardadas correctamente', 'success');
        this.completed.emit();
      },

      error: (error) => {
        this.toast.show('Error al guardar las afiliaciones', 'error');
        console.error(error);
      },
    });
  }

  loadCatalogs(): void {
    this.hrRepository.getEps().subscribe((data) => {
      this.eps = data;
    });

    this.hrRepository.getArls().subscribe((data) => {
      this.arls = data;
    });

    this.hrRepository.getPensionFunds().subscribe((data) => {
      this.pensionFunds = data;
    });

    this.hrRepository.getSeveranceFunds().subscribe((data) => {
      this.severanceFunds = data;
    });
  }
}
