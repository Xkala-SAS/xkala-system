import { Component } from '@angular/core';

import { RouterLink } from '@angular/router';

import { KpiCard } from '../../../../dashboard/presentation/components/kpi-card/kpi-card';

@Component({
  selector: 'app-hr',

  standalone: true,

  imports: [RouterLink, KpiCard],

  templateUrl: './hr.html',

  styleUrl: './hr.scss',
})
export class Hr {}
