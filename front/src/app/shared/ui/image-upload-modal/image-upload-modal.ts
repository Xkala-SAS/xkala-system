import { Component, input, output } from '@angular/core';

import { CommonModule } from '@angular/common';

import { Modal } from '../modal/modal';

@Component({
  selector: 'app-image-upload-modal',

  standalone: true,

  imports: [CommonModule, Modal],

  templateUrl: './image-upload-modal.html',

  styleUrl: './image-upload-modal.scss',
})
export class ImageUploadModal {
  visible = input<boolean>(false);

  title = input<string>('Cambiar imagen');

  previewUrl = input<string | null>(null);

  fileSelected = output<File>();
  
  save = output<void>();

  closed = output<void>();

  onFileChange(event: Event): void {
    const input = event.target as HTMLInputElement;

    if (!input.files?.length) {
      return;
    }

    this.fileSelected.emit(input.files[0]);
  }

  close(): void {
    this.closed.emit();
  }
}
