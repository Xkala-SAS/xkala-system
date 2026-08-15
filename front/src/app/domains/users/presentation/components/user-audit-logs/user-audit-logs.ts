import { Component, OnInit, inject, input } from '@angular/core';

import { CommonModule } from '@angular/common';

import { UserAuditLog } from '../../../domain/models/user-audit-log.model';

import { GetUserAuditLogsUseCase } from '../../../application/use-cases/get-user-audit-logs.use-case';

@Component({
  selector: 'app-user-audit-logs',

  standalone: true,

  imports: [CommonModule],

  templateUrl: './user-audit-logs.html',

  styleUrl: './user-audit-logs.scss',
})
export class UserAuditLogs implements OnInit {
  userId = input.required<string>();

  private getUserAuditLogsUseCase = inject(GetUserAuditLogsUseCase);

  logs: UserAuditLog[] = [];

  loading = false;

  selectedLog: UserAuditLog | null = null;

  showDetailModal = false;

  ngOnInit(): void {
    this.loadLogs();
  }

  loadLogs(): void {
    this.loading = true;

    this.getUserAuditLogsUseCase.execute(this.userId()).subscribe({
      next: (logs) => {
        this.logs = logs;

        this.loading = false;
      },

      error: (error) => {
        console.error(error);

        this.loading = false;
      },
    });
  }

  openDetail(log: UserAuditLog): void {
    this.selectedLog = log;

    this.showDetailModal = true;
  }

  closeDetail(): void {
    this.showDetailModal = false;

    this.selectedLog = null;
  }

  getStatusClass(status: number): string {
    if (status >= 200 && status < 300) {
      return 'bg-success';
    }

    if (status >= 400 && status < 500) {
      return 'bg-warning text-dark';
    }

    if (status >= 500) {
      return 'bg-danger';
    }

    return 'bg-secondary';
  }
}
