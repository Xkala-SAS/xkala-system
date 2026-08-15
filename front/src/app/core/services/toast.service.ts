import { Injectable, signal } from '@angular/core';

@Injectable({
  providedIn: 'root',
})
export class ToastService {
  visible = signal(false);

  message = signal('');

  type = signal<'success' | 'error' | 'warning'>('success');

  show(message: string, type: 'success' | 'error' | 'warning' = 'success'): void {
    this.message.set(message);

    this.type.set(type);

    this.visible.set(true);

    setTimeout(() => {
      this.visible.set(false);
    }, 4000);
  }
}
