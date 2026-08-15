import { Injectable, inject } from '@angular/core';

import { HttpClient } from '@angular/common/http';

import { API_CONFIG } from '../../../../core/config/api.config';

import { map } from 'rxjs';

import { City } from '../../domain/models/city.model';

import { AddressRequest } from '../../domain/models/address-request.model';

import { ContactsRequest } from '../../domain/models/contact-request.model';

import { HealthInfoRequest } from '../../domain/models/health-info-request.model';

import { SizeRequest } from '../../domain/models/size-request.model';

import { SavePersonalInfoRequest } from '../../domain/models/save-personal-info-request.model';

@Injectable({
  providedIn: 'root',
})
export class OnboardingHttpRepository {
  private http = inject(HttpClient);

  getStatus() {
    return this.http.get(`${API_CONFIG.baseUrl}/users/me/onboarding-status`);
  }

  savePersonalInfo(request: SavePersonalInfoRequest) {
    return this.http.post(`${API_CONFIG.baseUrl}/users/me/personal-info`, request);
  }

  getCities() {
    return this.http
      .get<any>(`${API_CONFIG.baseUrl}/cities`)
      .pipe(map((response) => response.data));
  }

  saveAddress(request: AddressRequest) {
    return this.http.post(`${API_CONFIG.baseUrl}/users/me/address`, request);
  }

  saveContacts(request: ContactsRequest) {
    return this.http.post(`${API_CONFIG.baseUrl}/users/me/contacts`, request);
  }

  saveHealthInfo(request: HealthInfoRequest) {
    return this.http.post(`${API_CONFIG.baseUrl}/users/me/health-info`, request);
  }

  saveSizes(request: SizeRequest) {
    return this.http.post(`${API_CONFIG.baseUrl}/users/me/sizes`, request);
  }

  uploadProfilePhoto(file: File) {
    const formData = new FormData();

    formData.append('file', file);

    return this.http.post(`${API_CONFIG.baseUrl}/users/upload/profile-photo`, formData);
  }

  uploadSignature(file: File) {
    const formData = new FormData();

    formData.append('file', file);

    return this.http.post(`${API_CONFIG.baseUrl}/users/upload/signature`, formData);
  }
}
