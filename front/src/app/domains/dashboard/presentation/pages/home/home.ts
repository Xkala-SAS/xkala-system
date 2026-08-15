import { Component, OnInit, inject } from '@angular/core';

import { KpiCard } from '../../components/kpi-card/kpi-card';
import { QuickActionCard } from '../../components/quick-action-card/quick-action-card';
import { ActivityCard } from '../../components/activity-card/activity-card';

import { GetTiDashboardUseCase } from '../../../application/use-cases/get-ti-dashboard.use-case';
import { TiDashboard } from '../../../domain/models/ti-dashboard.model';

@Component({
  selector: 'app-home',

  standalone: true,

  imports: [KpiCard, QuickActionCard, ActivityCard],

  templateUrl: './home.html',

  styleUrl: './home.scss',
})
export class Home implements OnInit {
  private getTiDashboardUseCase = inject(GetTiDashboardUseCase);

  dashboard: TiDashboard | null = null;

  loading = false;

  ngOnInit(): void {
    this.loadDashboard();
  }

  loadDashboard(): void {
    this.loading = true;

    this.getTiDashboardUseCase.execute().subscribe({
      next: (dashboard) => {
        this.dashboard = dashboard;

        this.loading = false;
      },

      error: (error) => {
        console.error(error);

        this.loading = false;
      },
    });
  }
}
