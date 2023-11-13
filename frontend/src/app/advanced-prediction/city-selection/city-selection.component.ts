import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-city-selection',
  templateUrl: './city-selection.component.html',
  styleUrls: ['./city-selection.component.css']
})
export class CitySelectionComponent {
  constructor(private router: Router) {}

  onSelectCity(city: string): void {
    this.router.navigate([`/weather/${city}`]);
  }
}
