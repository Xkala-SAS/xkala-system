import { Component, OnInit, inject } from '@angular/core';

import { CatalogList } from '../../components/catalog-list/catalog-list';

import { HrHttpRepository } from '../../../infrastructure/repositories/hr-http.repository';

import { CatalogItem } from '../../../domain/models/catalog-item.model';

@Component({
  selector: 'app-contract-types',

  standalone: true,

  imports: [CatalogList],

  templateUrl: './contract-types.html',
})
export class ContractTypes implements OnInit {
  private repository = inject(HrHttpRepository);

  items: CatalogItem[] = [];

  columns = [{ field: 'nombre', header: 'Nombre' }];

  ngOnInit(): void {
    this.repository.getContractTypes().subscribe({
      next: (data) => (this.items = data),
      error: console.error,
    });
  }
}
