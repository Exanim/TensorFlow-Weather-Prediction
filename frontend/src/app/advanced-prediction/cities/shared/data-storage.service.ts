import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Root } from './get-all-request.model';
import { environment } from 'src/environments/environment';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';
import { City } from './city.model';

@Injectable({
  providedIn: 'root',
})
export class DataStorageService {
  constructor(private http2: HttpClient) {}

  getGeoLocationByCityName(cityName: string): Observable<Root> {
    return this.http2
      .get<Root>(
        `http://api.openweathermap.org/geo/1.0/direct?q=${cityName}&appid=${environment.API_KEY}`
      )
      .pipe(
        map((response: Root) => {
          const cityInformation: City = {} as City;
          response.weather[0].icon = cityInformation.icon;
          response.name = cityInformation.name;
          response.main.temp = cityInformation.temp;
          response.main.humidity = cityInformation.humidity;
          response.wind.speed = cityInformation.wind;
          return response;
        })
      );
  }
}
