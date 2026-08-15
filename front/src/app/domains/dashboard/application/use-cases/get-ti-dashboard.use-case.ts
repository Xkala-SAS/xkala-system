import { Injectable, inject } from '@angular/core';

import { Observable } from 'rxjs';

import { DashboardHttpRepository } from '../../infrastructure/repositories/dashboard-http.repository';

import { TiDashboard } from '../../domain/models/ti-dashboard.model';

@Injectable({
  providedIn: 'root',
})
export class GetTiDashboardUseCase {
  private repository = inject(DashboardHttpRepository);

  execute(): Observable<TiDashboard> {
    return this.repository.getTiDashboard();
  }
}
