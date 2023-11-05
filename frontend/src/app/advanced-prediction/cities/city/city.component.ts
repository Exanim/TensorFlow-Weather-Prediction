import { Component, Input, OnInit } from '@angular/core';
import { City } from '../shared/city.model';
import { DataStorageService } from '../shared/data-storage.service';
import { Subscription } from 'rxjs';
import { Coord } from '../shared/get-all-request.model';

@Component({
  selector: 'app-city',
  templateUrl: './city.component.html',
  styleUrls: ['./city.component.css'],
})
export class CityComponent implements OnInit {
  city: City = {
    name: '',
    icon: '',
    temp: 0,
    humidity: 0,
    wind: 0,
    temperatureType: false,
  };

  @Input() cityName = '';

  constructor(private http: DataStorageService) {}

  ngOnInit(): void {
    this.city.name = this.cityName;
    this.subscriptionToCities = this.http
      .getGeoLocationByCityName(this.cityName)
      .subscribe((response) => {
        this.geoData = response;
        this.http
          .getCityInformationByGeoData(this.geoData)
          .subscribe((response) => {
            console.log(response);
            this.city = response;
          });
      });
  }
  subscriptionToCities: Subscription = new Subscription();
  geoData: Coord = { lon: 0, lat: 0 };
  cities: City[] = [];

  ngOnDestroy(): void {
    this.subscriptionToCities.unsubscribe();
  }
}
