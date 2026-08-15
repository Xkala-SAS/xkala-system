import { Observable } from 'rxjs';

import { User } from '../models/user.model';

export abstract class UsersRepository {
  abstract getUsers(): Observable<User[]>;
}
