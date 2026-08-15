import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root',
})
export class SessionService {
  private ACCESS_TOKEN = 'access_token';

  setAccessToken(token: string): void {
    localStorage.setItem(this.ACCESS_TOKEN, token);
  }

  getAccessToken(): string | null {
    return localStorage.getItem(this.ACCESS_TOKEN);
  }

  isAuthenticated(): boolean {
    return !!this.getAccessToken();
  }

  clearSession(): void {
    localStorage.clear();
  }
}
