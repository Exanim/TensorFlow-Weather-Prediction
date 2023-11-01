import { Component, OnInit } from '@angular/core';
import { CardDataService } from './card/card-data.service';
import { Card } from './card/card.model';
import { DataStorageService } from './shared/data-storage.service';

@Component({
  selector: 'app-simple-prediction',
  templateUrl: './simple-prediction.component.html',
  styleUrls: ['./simple-prediction.component.css'],
})
export class SimplePredictionComponent implements OnInit {
  cards: Card[] = [];
  city = '';
  fetchedCityName?: string;
  showEachPack = false;
  formerCity = '';
  isFetching = true;
  isFahrenheit: boolean = false;

  ngOnInit(): void {
    this.cards = this.cardData.getCardsData();
    this.cardData.onWeatherChanged.subscribe(
      (cardData) => (this.cards = cardData)
    );
    this.dataStorage.onFetchError.subscribe(
      (errorMessage) => (this.fetchedCityName = errorMessage)
    );
    this.dataStorage.isFetching.subscribe(
      (fetchBoolean) => (this.isFetching = fetchBoolean)
    );
  }

  constructor(
    private cardData: CardDataService,
    private dataStorage: DataStorageService
  ) {}

  onLookUpCity(): void {
    if (this.formerCity !== this.city && this.city) {
      this.dataStorage.getGeoLocationByCityName(this.city);
      this.fetchedCityName = this.city;
      this.formerCity = this.city;
      this.city = '';
      this.showEachPack = !this.showEachPack;
    }
  }

  onCheckboxChange(): void {
    this.cardData.setIsFahrenheit(this.isFahrenheit);
    this.cardData.UpdateTemperature();
  }
}
