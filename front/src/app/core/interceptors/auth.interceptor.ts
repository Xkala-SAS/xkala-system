import { HttpInterceptorFn } from '@angular/common/http';

import { inject } from '@angular/core';

import { SessionService } from '../../domains/auth/infrastructure/services/session.service';

export const authInterceptor: HttpInterceptorFn = (req, next) => {
  const sessionService = inject(SessionService);

  const token = sessionService.getAccessToken();

  if (token) {
    req = req.clone({
      setHeaders: {
        Authorization: `Bearer ${token}`,
      },
    });
  }

  return next(req);
};
