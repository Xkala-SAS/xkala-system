import { Component, Input } from '@angular/core';

import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-quick-action-card',

  standalone: true,

  imports: [CommonModule],

  templateUrl: './quick-action-card.html',

  styleUrl: './quick-action-card.scss',
})
export class QuickActionCard {
  @Input() title = '';

  @Input() subtitle = '';

  @Input() icon = '';
}
