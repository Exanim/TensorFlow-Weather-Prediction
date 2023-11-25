import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-day',
  templateUrl: './day.component.html',
  styleUrls: ['./day.component.css'],
})
export class DayComponent implements OnInit {
  city: { name: string } = { name: 'New York' };
  constructor() {}
  ngOnInit(): void {}
}
