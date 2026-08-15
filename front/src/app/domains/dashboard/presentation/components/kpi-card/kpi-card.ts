import { Component, Input } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-kpi-card',

  standalone: true,

  imports: [CommonModule],

  templateUrl: './kpi-card.html',

  styleUrl: './kpi-card.scss',
})
export class KpiCard {
  @Input() title = '';

  @Input() value: number | string = 0;

  @Input() icon = '';
}
