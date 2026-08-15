import { Component, input } from '@angular/core';

import { DataTable } from '../../../../../shared/ui/data-table/data-table';
import { PageHeader } from '../../../../../shared/ui/page-header/page-header';

@Component({
  selector: 'app-catalog-list',

  standalone: true,

  imports: [PageHeader, DataTable],

  templateUrl: './catalog-list.html',
})
export class CatalogList {
  title = input.required<string>();

  subtitle = input.required<string>();

  columns = input.required<any[]>();

  data = input.required<any[]>();
}
