import { Component, OnInit, inject } from '@angular/core';

import { CatalogList } from '../../components/catalog-list/catalog-list';

import { HrHttpRepository } from '../../../infrastructure/repositories/hr-http.repository';

@Component({
  selector: 'app-positions',

  standalone: true,

  imports: [CatalogList],

  templateUrl: './positions.html',
})
export class Positions implements OnInit {
  private repository = inject(HrHttpRepository);

  items: any[] = [];

  columns = [
    {
      field: 'nombre',
      header: 'Nombre',
    },

    {
      field: 'descripcion',
      header: 'Descripción',
    },
  ];

  ngOnInit(): void {
    this.repository.getPositions().subscribe({
      next: (data) => (this.items = data),
      error: console.error,
    });
  }
}
