import { MenuItem } from '../models/menu-item.model';

export const MENU_ITEMS: MenuItem[] = [
  {
    label: 'Mi Cuenta',
    icon: 'bi-person-circle',
    route: '/dashboard/my-account',
  },
  {
    label: 'Inicio',
    icon: 'bi-house',
    route: '/dashboard',
  },

  {
    label: 'Dashboard',
    icon: 'bi-grid',
    route: '/dashboard',
    permission: 'view_dashboard',
  },

  {
    label: 'RRHH',
    icon: 'bi-people',
    permission: 'view_users',

    children: [
      {
        label: 'Inicio',
        icon: 'bi-house',
        route: '/dashboard/rrhh',
        permission: 'view_users',
      },

      {
        label: 'Usuarios',
        icon: 'bi-person',
        route: '/dashboard/users',
        permission: 'view_users',
      },

      {
        label: 'Catálogos',
        icon: 'bi-journal-text',
        route: '/dashboard/hr-catalogs',
        permission: 'view_hr_catalogs',
      },
    ],
  },

  {
    label: 'Seguridad',
    icon: 'bi-shield-lock',

    children: [
      {
        label: 'Roles',
        icon: 'bi-person-badge',
        route: '/dashboard/security/roles',
        permission: 'view_roles',
      },

      {
        label: 'Permisos',
        icon: 'bi-key',
        route: '/dashboard/security/permissions',
        permission: 'view_permissions',
      },
    ],
  },
];
