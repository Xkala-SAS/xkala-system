import { Component, OnInit, inject } from '@angular/core';

import { CommonModule } from '@angular/common';

import { GetPermissionsUseCase } from '../../../application/use-cases/get-permissions.use-case';

import { Permission } from '../../../domain/models/permission.model';

@Component({
  selector: 'app-permissions',

  standalone: true,

  imports: [CommonModule],

  templateUrl: './permissions.html',

  styleUrl: './permissions.scss',
})
export class Permissions implements OnInit {
  private getPermissionsUseCase = inject(GetPermissionsUseCase);

  permissions: Permission[] = [];

  ngOnInit(): void {
    this.loadPermissions();
  }

  loadPermissions(): void {
    this.getPermissionsUseCase.execute().subscribe({
      next: (permissions) => {
        this.permissions = permissions;
      },
    });
  }
}
