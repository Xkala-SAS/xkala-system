import { Component, inject, OnInit } from '@angular/core';

import { ToastService } from '../../../../../core/services/toast.service';
import { PageHeader } from '../../../../../shared/ui/page-header/page-header';
import { DataTable } from '../../../../../shared/ui/data-table/data-table';
import { Loading } from '../../../../../shared/ui/loading/loading';
import { GetUsersUseCase } from '../../../application/use-cases/get-users.use-case';
import { FormsModule } from '@angular/forms';
import { Modal } from '../../../../../shared/ui/modal/modal';
import { User } from '../../../domain/models/user.model';
import { CreateUserForm } from '../../components/create-user-form/create-user-form';
import { EditUserForm } from '../../components/edit-user-form/edit-user-form';
import { DeleteUserUseCase } from '../../../application/use-cases/delete-user.use-case';
import { UserProfile } from '../../components/user-profile/user-profile';
import { ConfirmDialog } from '../../../../../shared/ui/confirm-dialog/confirm-dialog';
import { ExcelService } from '../../../../../core/services/excel.service';
import { RestoreUserUseCase } from '../../../application/use-cases/restore-user.use-case';

@Component({
  selector: 'app-users',

  standalone: true,

  imports: [
    PageHeader,
    DataTable,
    Loading,
    FormsModule,
    Modal,
    CreateUserForm,
    EditUserForm,
    ConfirmDialog,
    UserProfile,
  ],

  templateUrl: './users.html',

  styleUrl: './users.scss',
})
export class Users implements OnInit {
  private getUsersUseCase = inject(GetUsersUseCase);
  private deleteUserUseCase = inject(DeleteUserUseCase);
  private toastService = inject(ToastService);
  private excelService = inject(ExcelService);
  private restoreUserUseCase = inject(RestoreUserUseCase);

  columns = [
    {
      field: 'nombre',
      header: 'Nombre',
    },

    {
      field: 'email',
      header: 'Correo',
    },

    {
      field: 'estado',
      header: 'Estado',
    },
  ];

  users: User[] = [];

  loading = false;

  currentPage = 1;

  limit = 10;

  totalPages = 1;

  searchTerm = '';

  showCreateModal = false;

  selectedUser: any = null;

  showEditModal = false;

  showDeleteDialog = false;

  userToDelete: User | null = null;

  showViewModal = false;

  selectedUserId = '';

  statusFilter = '';

  orderBy = 'created_at';

  direction = 'desc';

  showRestoreDialog = false;

  userToRestore: User | null = null;

  ngOnInit(): void {
    this.loadUsers();
  }

  loadUsers(): void {
    this.loading = true;

    this.getUsersUseCase
      .execute(
        this.currentPage,
        this.limit,
        this.searchTerm,
        this.getStatusFilter(),
        this.orderBy,
        this.direction,
      )
      .subscribe({
        next: (response) => {
          this.users = response.data;

          this.totalPages = response.pagination.pages;

          this.loading = false;
        },

        error: (error) => {
          console.error(error);

          this.loading = false;
        },
      });
  }

  private getStatusFilter(): boolean | undefined {
    if (this.statusFilter === '') {
      return undefined;
    }

    return this.statusFilter === 'true';
  }

  onUserCreated(): void {
    this.closeCreateModal();

    this.loadUsers();
  }

  search(): void {
    this.currentPage = 1;

    this.loadUsers();
  }

  nextPage(): void {
    if (this.currentPage < this.totalPages) {
      this.currentPage++;

      this.loadUsers();
    }
  }

  previousPage(): void {
    if (this.currentPage > 1) {
      this.currentPage--;

      this.loadUsers();
    }
  }

  onUserUpdated(): void {
    this.closeEditModal();

    this.loadUsers();
  }

  openCreateModal(): void {
    this.showCreateModal = true;
  }

  closeCreateModal(): void {
    this.showCreateModal = false;
  }

  openEditModal(user: any): void {
    this.selectedUser = user;

    this.showEditModal = true;
  }

  closeEditModal(): void {
    this.showEditModal = false;

    this.selectedUser = null;
  }

  confirmDelete(user: User): void {
    this.userToDelete = user;

    this.showDeleteDialog = true;
  }

  deleteUser(): void {
    if (!this.userToDelete) {
      return;
    }

    this.deleteUserUseCase.execute(this.userToDelete.id).subscribe({
      next: () => {
        this.toastService.show('Usuario eliminado correctamente', 'success');

        this.showDeleteDialog = false;

        this.userToDelete = null;

        this.loadUsers();
      },

      error: (error) => {
        console.error(error);

        this.toastService.show('Error eliminando usuario', 'error');
      },
    });
  }

  closeDeleteDialog(): void {
    this.showDeleteDialog = false;

    this.userToDelete = null;
  }

  openViewModal(user: User): void {
    this.selectedUserId = user.id;

    this.showViewModal = true;
  }

  closeViewModal(): void {
    this.showViewModal = false;

    this.selectedUserId = '';
  }

  onOrderChange(): void {
    this.currentPage = 1;

    this.loadUsers();
  }

  exportUsers(): void {
    const data = this.users.map((user) => ({
      Nombre: user.nombre,

      Correo: user.email,

      Estado: user.estado ? 'Activo' : 'Inactivo',
    }));

    this.excelService.export(data, 'usuarios');
  }

  confirmRestore(user: User): void {
    this.userToRestore = user;

    this.showRestoreDialog = true;
  }

  restoreUser(): void {
    if (!this.userToRestore) {
      return;
    }

    this.restoreUserUseCase.execute(this.userToRestore.id).subscribe({
      next: () => {
        this.toastService.show('Usuario reactivado correctamente', 'success');

        this.showRestoreDialog = false;

        this.userToRestore = null;

        this.loadUsers();
      },

      error: () => {
        this.toastService.show('Error reactivando usuario', 'error');
      },
    });
  }
  closeRestoreDialog(): void {
    this.showRestoreDialog = false;

    this.userToRestore = null;
  }
}
