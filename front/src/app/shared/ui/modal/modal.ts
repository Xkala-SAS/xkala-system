import { Component, input, output } from '@angular/core';
import { NgClass } from '@angular/common';

@Component({
  selector: 'app-modal',

  standalone: true,

  imports: [NgClass],

  templateUrl: './modal.html',

  styleUrl: './modal.scss',
})
export class Modal {
  visible = input<boolean>(false);

  title = input<string>('');

  closed = output<void>();

  size = input<'sm' | 'md' | 'lg' | 'xl' | 'full'>('md');

  close(): void {
    this.closed.emit();
  }
}
