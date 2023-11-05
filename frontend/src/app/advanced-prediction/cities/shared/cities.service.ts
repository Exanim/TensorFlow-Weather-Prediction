import { Injectable } from '@angular/core';
import { City } from './city.model';

@Injectable({
  providedIn: 'root'
})
export class CitiesService {

  constructor() { }

  cities: City[] = [];
}
