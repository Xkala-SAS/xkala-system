import { Component, input, output } from '@angular/core';

@Component({
  selector: 'app-page-header',

  standalone: true,

  templateUrl: './page-header.html',

  styleUrl: './page-header.scss',
})
export class PageHeader {
  title = input.required<string>();

  subtitle = input<string>('');

  buttonText = input<string>('');

  buttonClicked = output<void>();

  onButtonClick(): void {
    this.buttonClicked.emit();
  }
}
