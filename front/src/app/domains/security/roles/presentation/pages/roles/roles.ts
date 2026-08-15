import { Component, OnInit, inject } from '@angular/core';

import { CommonModule } from '@angular/common';

import { RouterLink } from '@angular/router';

import { GetRolesUseCase } from '../../../application/use-cases/get-roles.use-case';

import { Role } from '../../../domain/models/role.model';

@Component({
  selector: 'app-roles',

  standalone: true,

  imports: [CommonModule, RouterLink],

  templateUrl: './roles.html',

  styleUrl: './roles.scss',
})
export class Roles implements OnInit {
  private getRolesUseCase = inject(GetRolesUseCase);

  roles: Role[] = [];

  loading = false;

  ngOnInit(): void {
    this.loadRoles();
  }

  loadRoles(): void {
    this.loading = true;

    this.getRolesUseCase.execute().subscribe({
      next: (roles) => {
        this.roles = roles;

        this.loading = false;
      },

      error: (error) => {
        console.error(error);

        this.loading = false;
      },
    });
  }
}
