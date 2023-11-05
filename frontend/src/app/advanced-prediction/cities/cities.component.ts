import { Component, OnDestroy, OnInit } from '@angular/core';
import { City } from './shared/city.model';
import { DataStorageService } from './shared/data-storage.service';
import { Coord } from './shared/get-all-request.model';
import { Subscription } from 'rxjs';

@Component({
  selector: 'app-cities',
  templateUrl: './cities.component.html',
  styleUrls: ['./cities.component.css'],
})
export class CitiesComponent {

}
