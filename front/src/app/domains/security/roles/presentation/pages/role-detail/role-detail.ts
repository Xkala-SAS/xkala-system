import { Component, OnInit, inject } from '@angular/core';

import { CommonModule } from '@angular/common';

import { ActivatedRoute } from '@angular/router';

import { RoleDetail } from '../../../domain/models/role-detail.model';

import { GetRoleDetailUseCase } from '../../../application/use-cases/get-role-detail.use-case';

@Component({
  selector: 'app-role-detail',

  standalone: true,

  imports: [CommonModule],

  templateUrl: './role-detail.html',

  styleUrl: './role-detail.scss',
})
export class RoleDetailComponent implements OnInit {
  private route = inject(ActivatedRoute);

  private getRoleDetailUseCase = inject(GetRoleDetailUseCase);

  role: RoleDetail | null = null;

  loading = false;

  ngOnInit(): void {
    const roleId = this.route.snapshot.paramMap.get('id');

    if (!roleId) {
      return;
    }

    this.loading = true;

    this.getRoleDetailUseCase.execute(roleId).subscribe({
      next: (role) => {
        this.role = role;

        this.loading = false;
      },

      error: (error) => {
        console.error(error);

        this.loading = false;
      },
    });
  }
}
