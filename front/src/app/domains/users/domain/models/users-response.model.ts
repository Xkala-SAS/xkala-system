import { User } from './user.model';

import { Pagination } from '../../../../shared/models/pagination.model';

export interface UsersResponse {
  data: User[];

  pagination: Pagination;
}
