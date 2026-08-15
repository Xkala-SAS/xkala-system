import { Component, input, output } from '@angular/core';

@Component({
  selector: 'app-data-table',

  standalone: true,

  imports: [],

  templateUrl: './data-table.html',

  styleUrl: './data-table.scss',
})
export class DataTable {
  viewClicked = output<any>();

  editClicked = output<any>();

  deleteClicked = output<any>();

  restoreClicked = output<any>();

  columns = input.required<
    {
      field: string;
      header: string;
    }[]
  >();

  data = input.required<any[]>();

  actions = input<boolean>(false);
}
