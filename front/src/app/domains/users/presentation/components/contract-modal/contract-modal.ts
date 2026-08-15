import { Component, inject, input, output, OnInit, OnChanges, SimpleChanges } from '@angular/core';
import { CommonModule } from '@angular/common';

import { Modal } from '../../../../../shared/ui/modal/modal';

import { FormBuilder, ReactiveFormsModule, Validators } from '@angular/forms';

import { CatalogItem } from '../../../../hr/domain/models/catalog-item.model';

import { HrHttpRepository } from '../../../../hr/infrastructure/repositories/hr-http.repository';

import { CreateUserContractUseCase } from '../../../application/use-cases/create-user-contract.use-case';

import { UpdateUserContractUseCase } from '../../../application/use-cases/update-user-contract.use-case';

import { ToastService } from '../../../../../core/services/toast.service';

import { GetUserContractUseCase } from '../../../application/use-cases/get-user-contract.use-case';

@Component({
  selector: 'app-contract-modal',

  standalone: true,

  imports: [Modal, ReactiveFormsModule, CommonModule],

  templateUrl: './contract-modal.html',

  styleUrl: './contract-modal.scss',
})
export class ContractModal implements OnInit, OnChanges {
  private fb = inject(FormBuilder);

  private hrRepository = inject(HrHttpRepository);

  private createContractUseCase = inject(CreateUserContractUseCase);

  private updateContractUseCase = inject(UpdateUserContractUseCase);

  private toast = inject(ToastService);

  private getContractUseCase = inject(GetUserContractUseCase);

  visible = input<boolean>(false);

  isEdit = input<boolean>(false);

  userId = input.required<string>();

  closed = output<void>();

  saved = output<void>();

  positions: any[] = [];

  contractTypes: CatalogItem[] = [];

  form = this.fb.group({
    position_id: ['', Validators.required],

    contract_type_id: ['', Validators.required],

    fecha_ingreso: ['', Validators.required],

    remuneration_type: ['MONTHLY', Validators.required],

    remuneration_value: [0, Validators.required],

    estado_laboral: [true],
  });

  ngOnInit(): void {
    this.loadPositions();

    this.loadContractTypes();
  }

  ngOnChanges(changes: SimpleChanges): void {
    if (changes['visible'] && this.visible() && this.isEdit()) {
      this.loadContract();
    }
  }

  close(): void {
    this.closed.emit();
  }

  loadPositions(): void {
    this.hrRepository.getPositions().subscribe({
      next: (data) => {
        this.positions = data;
      },
    });
  }

  loadContractTypes(): void {
    this.hrRepository.getContractTypes().subscribe({
      next: (data) => {
        this.contractTypes = data;
      },
    });
  }

  save(): void {
    if (this.form.invalid) {
      this.form.markAllAsTouched();

      return;
    }

    const payload = this.form.getRawValue();

    if (this.isEdit()) {
      this.updateContractUseCase.execute(this.userId(), payload as any).subscribe({
        next: () => {
          this.toast.show('Contrato actualizado correctamente', 'success');

          this.saved.emit();

          this.close();
        },

        error: (error) => {
          this.toast.show(error?.error?.message || 'Error actualizando contrato', 'error');
        },
      });

      return;
    }

    this.createContractUseCase.execute(this.userId(), payload as any).subscribe({
      next: () => {
        this.toast.show('Contrato creado correctamente', 'success');

        this.saved.emit();

        this.close();
      },

      error: (error) => {
        this.toast.show(error?.error?.message || 'Error creando contrato', 'error');
      },
    });
  }

  loadContract(): void {
    this.getContractUseCase.execute(this.userId()).subscribe({
      next: (contract) => {
        this.form.patchValue({
          position_id: contract.position_id,

          contract_type_id: contract.contract_type_id,

          fecha_ingreso: contract.fecha_ingreso?.split('T')[0],

          remuneration_type: contract.remuneration_type,

          remuneration_value: contract.remuneration_value,

          estado_laboral: contract.estado_laboral,
        });
      },
    });
  }
}
