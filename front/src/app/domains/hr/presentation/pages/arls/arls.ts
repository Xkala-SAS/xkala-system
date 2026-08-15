import { Component, OnInit, inject } from '@angular/core';

import { CatalogList } from '../../components/catalog-list/catalog-list';

import { HrHttpRepository } from '../../../infrastructure/repositories/hr-http.repository';

import { CatalogItem } from '../../../domain/models/catalog-item.model';

@Component({
  selector: 'app-arls',

  standalone: true,

  imports: [CatalogList],

  templateUrl: './arls.html',
})
export class Arls implements OnInit {
  private repository = inject(HrHttpRepository);

  items: CatalogItem[] = [];

  columns = [
    {
      field: 'nombre',
      header: 'Nombre',
    },
  ];

  ngOnInit(): void {
    this.repository.getArls().subscribe({
      next: (data) => {
        this.items = data;
      },

      error: (error) => {
        console.error(error);
      },
    });
  }
}
