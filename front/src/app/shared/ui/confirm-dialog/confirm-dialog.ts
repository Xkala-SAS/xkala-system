import { Component, input, output } from '@angular/core';

import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-confirm-dialog',

  standalone: true,

  imports: [CommonModule],

  templateUrl: './confirm-dialog.html',

  styleUrl: './confirm-dialog.scss',
})
export class ConfirmDialog {
  visible = input<boolean>(false);

  title = input<string>('Confirmar acción');

  message = input<string>('¿Deseas continuar?');

  confirmed = output<void>();

  cancelled = output<void>();
}
