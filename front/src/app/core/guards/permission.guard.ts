import { inject } from '@angular/core';

import { ActivatedRouteSnapshot, CanActivateFn, Router } from '@angular/router';

import { CurrentUserService } from '../services/current-user.service';

export const permissionGuard: CanActivateFn = (route: ActivatedRouteSnapshot) => {
  const currentUserService = inject(CurrentUserService);

  const router = inject(Router);

  const permission = route.data['permission'];

  if (!permission) {
    return true;
  }

  if (currentUserService.hasPermission(permission)) {
    return true;
  }

  router.navigate(['/dashboard']);

  return false;
};
