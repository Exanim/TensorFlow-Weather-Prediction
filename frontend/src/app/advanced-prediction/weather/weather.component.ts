import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { DataStorageService } from './shared/data-storage.service';

@Component({
  selector: 'app-weather',
  templateUrl: './weather.component.html',
  styleUrls: ['./weather.component.css']
})
export class WeatherComponent implements OnInit {
  cityName: string = '';
  cityInformation: any;

  constructor(
    private route: ActivatedRoute,
    private dataStorageService: DataStorageService
  ) {}

  ngOnInit(): void {
    this.route.params.subscribe(params => {
      this.cityName = params['city'];
      this.fetchWeatherInformation();
    });
  }

  fetchWeatherInformation() {
    this.dataStorageService.getGeoLocationByCityName(this.cityName).subscribe(
      geoData => {
        this.dataStorageService.getCityInformationByGeoData(geoData).subscribe(
          cityInfo => {
            this.cityInformation = cityInfo;
          },
          error => {
            console.error('Error fetching city information:', error);
          }
        );
      },
      error => {
        console.error('Error fetching geo location:', error);
      }
    );
  }
}