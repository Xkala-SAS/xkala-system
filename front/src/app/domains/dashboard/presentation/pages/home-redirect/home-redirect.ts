import { Component, OnInit, inject } from '@angular/core';

import { Router } from '@angular/router';

import { CurrentUserService } from '../../../../../core/services/current-user.service';

@Component({
  selector: 'app-home-redirect',

  standalone: true,

  template: '',
})
export class HomeRedirect implements OnInit {
  private router = inject(Router);

  private currentUserService = inject(CurrentUserService);

  ngOnInit(): void {
    const permissions = this.currentUserService.user()?.permissions ?? [];

    if (permissions.includes('manage_permissions')) {
      this.router.navigate(['/dashboard/admin']);

      return;
    }

    if (permissions.includes('view_hr')) {
      this.router.navigate(['/dashboard/hr-home']);

      return;
    }

    this.router.navigate(['/dashboard/employee']);
  }
}
