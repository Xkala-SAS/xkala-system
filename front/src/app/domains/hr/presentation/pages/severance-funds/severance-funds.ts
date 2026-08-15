import { Component, OnInit, inject } from '@angular/core';

import { CatalogList } from '../../components/catalog-list/catalog-list';

import { HrHttpRepository } from '../../../infrastructure/repositories/hr-http.repository';

import { CatalogItem } from '../../../domain/models/catalog-item.model';

@Component({
  selector: 'app-severance-funds',

  standalone: true,

  imports: [CatalogList],

  templateUrl: './severance-funds.html',
})
export class SeveranceFunds implements OnInit {
  private repository = inject(HrHttpRepository);

  items: CatalogItem[] = [];

  columns = [{ field: 'nombre', header: 'Nombre' }];

  ngOnInit(): void {
    this.repository.getSeveranceFunds().subscribe({
      next: (data) => (this.items = data),
      error: console.error,
    });
  }
}
