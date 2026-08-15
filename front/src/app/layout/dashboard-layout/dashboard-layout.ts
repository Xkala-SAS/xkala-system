import { Component, inject, OnInit, computed } from '@angular/core';

import { CommonModule } from '@angular/common';

import { RouterLink, RouterLinkActive, RouterOutlet, Router } from '@angular/router';

import { LayoutService } from '../../core/services/layout.service';

import { MENU_ITEMS } from '../../core/config/menu.config';

import { MenuItem } from '../../core/models/menu-item.model';

import { SessionService } from '../../domains/auth/infrastructure/services/session.service';

import { GetUserProfileUseCase } from '../../domains/users/application/use-cases/get-user-profile.use-case';

import { UserProfile } from '../../domains/users/domain/models/user-profile.model';

import { API_CONFIG } from '../../core/config/api.config';

import {} from '@angular/core';

import { CurrentUserService } from '../../core/services/current-user.service';

@Component({
  selector: 'app-dashboard-layout',

  standalone: true,

  imports: [CommonModule, RouterOutlet, RouterLink, RouterLinkActive],

  templateUrl: './dashboard-layout.html',

  styleUrl: './dashboard-layout.scss',
})
export class DashboardLayout implements OnInit {
  layoutService = inject(LayoutService);

  private router = inject(Router);

  private sessionService = inject(SessionService);

  private getUserProfileUseCase = inject(GetUserProfileUseCase);

  currentUserService = inject(CurrentUserService);

  apiUrl = API_CONFIG.baseUrl;

  profile: UserProfile | null = null;

  sidebarOpen = false;

  menuItems = computed(() => {
    const permissions = this.currentUserService.user()?.permissions ?? [];

    return MENU_ITEMS.map((item) => {
      if (item.permission && !permissions.includes(item.permission)) {
        return null;
      }

      if (!item.children) {
        return item;
      }

      const children = item.children.filter(
        (child: MenuItem) => !child.permission || permissions.includes(child.permission),
      );

      return children.length
        ? {
            ...item,
            children,
          }
        : null;
    }).filter(Boolean) as MenuItem[];
  });

  ngOnInit(): void {
    this.getUserProfileUseCase.getMyProfile().subscribe({
      next: (profile) => {
        this.profile = profile;

        this.currentUserService.setUser(profile);
      },
    });
  }

  logout(): void {
    this.sessionService.clearSession();

    this.router.navigate(['/login']);
  }

  hasPermission(permission: string): boolean {
    return this.profile?.permissions?.includes(permission) ?? false;
  }

  toggleSidebar(): void {
    this.sidebarOpen = !this.sidebarOpen;
  }

  closeSidebar(): void {
    if (window.innerWidth <= 991) {
      this.sidebarOpen = false;
    }
  }
}
