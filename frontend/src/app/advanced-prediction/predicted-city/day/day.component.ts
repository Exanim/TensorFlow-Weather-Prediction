import { Component, Input, OnInit } from '@angular/core';

@Component({
  selector: 'app-day',
  templateUrl: './day.component.html',
  styleUrls: ['./day.component.css'],
})
export class DayComponent implements OnInit {
  @Input() day?: string;
  @Input() temperature?: number;
  @Input() humidity?: number;
  constructor() {}
  ngOnInit(): void {}
}
