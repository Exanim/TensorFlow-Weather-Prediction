import { Component, Input, OnInit } from '@angular/core';
import { City } from '../shared/city.model';

@Component({
  selector: 'app-city',
  templateUrl: './city.component.html',
  styleUrls: ['./city.component.css'],
})
export class CityComponent implements OnInit {
  @Input() city?: City;

  constructor() {}

  ngOnInit(): void {}
}
