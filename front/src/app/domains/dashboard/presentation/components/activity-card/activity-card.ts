import { Component } from '@angular/core';

import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-activity-card',

  standalone: true,

  imports: [CommonModule],

  templateUrl: './activity-card.html',

  styleUrl: './activity-card.scss',
})
export class ActivityCard {
  activities = [
    {
      title: 'Inicio de sesión',

      time: 'Hace 2 minutos',
    },

    {
      title: 'Nuevo usuario creado',

      time: 'Hace 15 minutos',
    },

    {
      title: 'Actualización de permisos',

      time: 'Hace 1 hora',
    },

    {
      title: 'Auditoría exportada',

      time: 'Hace 3 horas',
    },
  ];
}
