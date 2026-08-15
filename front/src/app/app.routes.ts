import { Routes } from '@angular/router';
import { authGuard } from './core/guards/auth.guard';
import { permissionGuard } from './core/guards/permission.guard';

export const routes: Routes = [
  {
    path: '',

    loadComponent: () => import('./layout/public-layout/public-layout').then((m) => m.PublicLayout),

    children: [
      {
        path: 'login',

        loadComponent: () =>
          import('./domains/auth/presentation/pages/login/login').then((m) => m.Login),
      },

      {
        path: '',

        redirectTo: 'login',

        pathMatch: 'full',
      },
    ],
  },

  {
    path: 'dashboard',

    canActivate: [authGuard],

    loadComponent: () =>
      import('./layout/dashboard-layout/dashboard-layout').then((m) => m.DashboardLayout),

    children: [
      {
        path: '',

        loadComponent: () =>
          import('./domains/dashboard/presentation/pages/home-redirect/home-redirect').then(
            (m) => m.HomeRedirect,
          ),
      },

      {
        path: 'admin',

        loadComponent: () =>
          import('./domains/dashboard/presentation/pages/home/home').then((m) => m.Home),
      },

      {
        path: 'hr',

        loadComponent: () =>
          import('./domains/dashboard/presentation/pages/home/home').then((m) => m.Home),
      },

      {
        path: 'management',

        loadComponent: () =>
          import('./domains/dashboard/presentation/pages/home/home').then((m) => m.Home),
      },

      {
        path: 'supervisor',

        loadComponent: () =>
          import('./domains/dashboard/presentation/pages/home/home').then((m) => m.Home),
      },

      {
        path: 'audit',

        loadComponent: () =>
          import('./domains/dashboard/presentation/pages/home/home').then((m) => m.Home),
      },

      {
        path: 'employee',

        loadComponent: () =>
          import('./domains/dashboard/presentation/pages/employee-home/employee-home').then(
            (m) => m.EmployeeHome,
          ),
      },

      {
        path: 'my-account',

        loadComponent: () =>
          import('./domains/account/presentation/pages/my-account/my-account').then(
            (m) => m.MyAccount,
          ),
      },

      {
        path: 'hr-home',

        loadComponent: () =>
          import('./domains/dashboard/presentation/pages/hr-home/hr-home').then((m) => m.HrHome),
      },

      {
        path: 'rrhh',

        canActivate: [permissionGuard],

        data: {
          permission: 'view_hr',
        },

        loadComponent: () => import('./domains/hr/presentation/pages/hr/hr').then((m) => m.Hr),
      },

      {
        path: 'users',

        canActivate: [permissionGuard],

        data: {
          permission: 'view_users',
        },

        loadComponent: () =>
          import('./domains/users/presentation/pages/users/users').then((m) => m.Users),
      },

      {
        path: 'hr-catalogs',

        canActivate: [permissionGuard],

        data: {
          permission: 'view_hr_catalogs',
        },

        loadComponent: () =>
          import('./domains/hr/presentation/pages/hr-catalogs/hr-catalogs').then(
            (m) => m.HrCatalogs,
          ),
      },

      {
        path: 'eps',

        loadComponent: () => import('./domains/hr/presentation/pages/eps/eps').then((m) => m.Eps),
      },

      {
        path: 'arls',

        loadComponent: () =>
          import('./domains/hr/presentation/pages/arls/arls').then((m) => m.Arls),
      },

      {
        path: 'pension-funds',

        loadComponent: () =>
          import('./domains/hr/presentation/pages/pension-funds/pension-funds').then(
            (m) => m.PensionFunds,
          ),
      },

      {
        path: 'severance-funds',

        loadComponent: () =>
          import('./domains/hr/presentation/pages/severance-funds/severance-funds').then(
            (m) => m.SeveranceFunds,
          ),
      },

      {
        path: 'contract-types',

        loadComponent: () =>
          import('./domains/hr/presentation/pages/contract-types/contract-types').then(
            (m) => m.ContractTypes,
          ),
      },

      {
        path: 'positions',

        loadComponent: () =>
          import('./domains/hr/presentation/pages/positions/positions').then((m) => m.Positions),
      },

      {
        path: 'security/roles',

        canActivate: [permissionGuard],

        data: {
          permission: 'view_roles',
        },

        loadComponent: () =>
          import('./domains/security/roles/presentation/pages/roles/roles').then((m) => m.Roles),
      },

      {
        path: 'security/roles/:id',

        canActivate: [permissionGuard],

        data: {
          permission: 'view_roles',
        },

        loadComponent: () =>
          import('./domains/security/roles/presentation/pages/role-detail/role-detail').then(
            (m) => m.RoleDetailComponent,
          ),
      },

      {
        path: 'security/permissions',

        canActivate: [permissionGuard],

        data: {
          permission: 'view_permissions',
        },

        loadComponent: () =>
          import('./domains/security/permissions/presentation/pages/permissions/permissions').then(
            (m) => m.Permissions,
          ),
      },
    ],
  },

  {
    path: 'onboarding',

    canActivate: [authGuard],

    loadComponent: () =>
      import('./domains/onboarding/presentation/pages/onboarding/onboarding').then(
        (m) => m.Onboarding,
      ),
  },

  {
    path: '**',

    redirectTo: 'login',
  },
];
