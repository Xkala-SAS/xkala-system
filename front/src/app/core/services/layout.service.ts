import { Injectable, signal } from '@angular/core';

@Injectable({
  providedIn: 'root',
})
export class LayoutService {
  sidebarOpen = signal(false);

  toggleSidebar(): void {
    this.sidebarOpen.update((value) => !value);
  }

  closeSidebar(): void {
    this.sidebarOpen.set(false);
  }

  openSidebar(): void {
    this.sidebarOpen.set(true);
  }
}
