import { Component, OnInit, inject } from '@angular/core';

import { CatalogList } from '../../components/catalog-list/catalog-list';

import { HrHttpRepository } from '../../../infrastructure/repositories/hr-http.repository';

import { CatalogItem } from '../../../domain/models/catalog-item.model';

@Component({
  selector: 'app-pension-funds',

  standalone: true,

  imports: [CatalogList],

  templateUrl: './pension-funds.html',
})
export class PensionFunds implements OnInit {
  private repository = inject(HrHttpRepository);

  items: CatalogItem[] = [];

  columns = [{ field: 'nombre', header: 'Nombre' }];

  ngOnInit(): void {
    this.repository.getPensionFunds().subscribe({
      next: (data) => (this.items = data),
      error: console.error,
    });
  }
}
