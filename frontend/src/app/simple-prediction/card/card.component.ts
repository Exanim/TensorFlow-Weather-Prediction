import { Component, Input, OnInit } from '@angular/core';
import { Card } from './card.model';

@Component({
  selector: 'app-card',
  templateUrl: './card.component.html',
  styleUrls: ['../simple-prediction.component.css'],
})
export class CardComponent implements OnInit {
  @Input() card: Card = new Card('', '', 0, false, 0, 0);

  constructor() {}

  ngOnInit(): void {}
}
