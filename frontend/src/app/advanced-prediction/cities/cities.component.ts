import { Component } from '@angular/core';

@Component({
  selector: 'app-cities',
  templateUrl: './cities.component.html',
  styleUrls: ['./cities.component.css'],
})
export class CitiesComponent {
  cities: string[] = ['Budapest', 'Sopron', 'Szeged', 'Nyíregyháza'];
}
