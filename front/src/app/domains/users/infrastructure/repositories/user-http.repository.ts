import { Injectable, inject } from '@angular/core';

import { HttpClient } from '@angular/common/http';

import { Observable, map } from 'rxjs';

import { API_CONFIG } from '../../../../core/config/api.config';

import { UsersResponse } from '../../domain/models/users-response.model';

import { CreateUserRequest } from '../../domain/models/create-user-request.model';

import { UserDetail } from '../../domain/models/user-detail.model';

import { UserProfile } from '../../domain/models/user-profile.model';

import { UserDocument } from '../../domain/models/user-document.model';

import { UserContract } from '../../domain/models/user-contract.model';

import { SaveUserContractRequest } from '../../domain/models/save-user-contract-request.model';

@Injectable({
  providedIn: 'root',
})
export class UsersHttpRepository {
  private http = inject(HttpClient);

  getUsers(
    page: number,
    limit: number,
    search: string = '',
    estado?: boolean,
    orderBy: string = 'created_at',
    direction: string = 'desc',
  ): Observable<UsersResponse> {
    let url = `${API_CONFIG.baseUrl}/users?page=${page}&limit=${limit}&search=${search}`;

    if (estado !== undefined) {
      url += `&estado=${estado}`;
    }

    url += `&order_by=${orderBy}`;
    url += `&direction=${direction}`;

    return this.http.get<any>(url).pipe(
      map((response) => ({
        data: response.data,
        pagination: response.pagination,
      })),
    );
  }

  createUser(data: CreateUserRequest): Observable<any> {
    return this.http.post(`${API_CONFIG.baseUrl}/users`, data);
  }

  getById(userId: string): Observable<UserDetail> {
    return this.http
      .get<any>(`${API_CONFIG.baseUrl}/users/${userId}`)
      .pipe(map((response) => response.data));
  }

  getProfile(userId: string): Observable<UserProfile> {
    return this.http.get<UserProfile>(`${API_CONFIG.baseUrl}/users/${userId}/profile`);
  }

  getDocuments(userId: string): Observable<UserDocument[]> {
    return this.http
      .get<any>(`${API_CONFIG.baseUrl}/users/${userId}/documents`)
      .pipe(map((response) => response.data));
  }

  updateUser(userId: string, data: any): Observable<any> {
    return this.http.put(`${API_CONFIG.baseUrl}/users/${userId}`, data);
  }

  deleteUser(userId: string): Observable<any> {
    return this.http.delete(`${API_CONFIG.baseUrl}/users/${userId}`);
  }

  uploadDocument(userId: string, documentType: string, file: File): Observable<any> {
    const formData = new FormData();

    formData.append('file', file);

    return this.http.post(
      `${API_CONFIG.baseUrl}/users/${userId}/documents?document_type=${documentType}`,
      formData,
    );
  }

  uploadSignature(userId: string, file: File): Observable<any> {
    const formData = new FormData();

    formData.append('file', file);

    return this.http.post(`${API_CONFIG.baseUrl}/users/${userId}/signature`, formData);
  }

  uploadProfilePhoto(userId: string, file: File): Observable<any> {
    const formData = new FormData();

    formData.append('file', file);

    return this.http.post(`${API_CONFIG.baseUrl}/users/${userId}/profile-photo`, formData);
  }

  deleteDocument(documentId: string): Observable<any> {
    return this.http.delete(`${API_CONFIG.baseUrl}/users/document/${documentId}`);
  }

  restoreUser(userId: string): Observable<any> {
    return this.http.patch(`${API_CONFIG.baseUrl}/users/${userId}/restore`, {});
  }

  getUserContract(userId: string): Observable<UserContract> {
    return this.http.get<UserContract>(`${API_CONFIG.baseUrl}/users/${userId}/contract`);
  }

  createUserContract(userId: string, data: SaveUserContractRequest): Observable<any> {
    return this.http.post(`${API_CONFIG.baseUrl}/users/${userId}/contract`, data);
  }

  updateUserContract(userId: string, data: SaveUserContractRequest): Observable<any> {
    return this.http.put(`${API_CONFIG.baseUrl}/users/${userId}/contract`, data);
  }

  getMyProfile(): Observable<UserProfile> {
    return this.http.get<UserProfile>(`${API_CONFIG.baseUrl}/users/profile`);
  }
}
