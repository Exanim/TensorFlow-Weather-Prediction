import { Component, OnInit } from '@angular/core';
import { City } from './shared/city.model';
import { DataStorageService } from './shared/data-storage.service';

@Component({
  selector: 'app-cities',
  templateUrl: './cities.component.html',
  styleUrls: ['./cities.component.css'],
})
export class CitiesComponent implements OnInit {
  constructor(private http: DataStorageService) {}
  ngOnInit(): void {
    this.http
      .getGeoLocationByCityName('')
      .subscribe((response) => console.log(response));
  }
  cities: City[] = [];
}
