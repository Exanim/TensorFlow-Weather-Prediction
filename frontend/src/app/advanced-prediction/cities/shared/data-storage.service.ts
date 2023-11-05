import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import {
  Coord,
  GeoAPIResponse,
  WeatherAPIResponse,
} from './get-all-request.model';
import { environment } from 'src/environments/environment';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';
import { City } from './city.model';

@Injectable({
  providedIn: 'root',
})
export class DataStorageService {
  constructor(private http2: HttpClient) {}

  getGeoLocationByCityName(cityName: string): Observable<Coord> {
    return this.http2
      .get<GeoAPIResponse[]>(
        `http://api.openweathermap.org/geo/1.0/direct?q=${cityName}&appid=${environment.API_KEY}`
      )
      .pipe(
        map((response: GeoAPIResponse[]) => {
          const geoInformation: Coord = {
            lon: response[0].lon,
            lat: response[0].lat,
          };
          return geoInformation;
        })
      );
  }

  getCityInformationByGeoData(geoData: Coord): Observable<City> {
    return this.http2
      .get<WeatherAPIResponse>(
        `http://api.openweathermap.org/data/2.5/weather?lat=${geoData.lat}&lon=${geoData.lon}&appid=${environment.API_KEY}&units=metric`
      )
      .pipe(
        map((response: WeatherAPIResponse) => {
          const cityInformation: City = {
            icon: response.weather[0].icon,
            name: response.name,
            temp: response.main.temp,
            humidity: response.main.humidity,
            wind: response.wind.speed * 3.6,
            temperatureType: false,
          };
          return cityInformation;
        })
      );
  }
}
