import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { SimplePredictionComponent } from './simple-prediction/simple-prediction.component';
import { FormsModule } from '@angular/forms';
import { CardComponent } from './simple-prediction/card/card.component';
import { HttpClientModule } from '@angular/common/http';
import { WelcomeScreenComponent } from './welcome-screen/welcome-screen.component';
import { CitiesComponent } from './advanced-prediction/cities/cities.component';
import { CityComponent } from './advanced-prediction/cities/city/city.component';
import { CitySelectionComponent } from './advanced-prediction/city-selection/city-selection.component';
import { WeatherComponent } from './advanced-prediction/weather/weather.component';
import { PredictedCityComponent } from './advanced-prediction/predicted-city/predicted-city.component';
import { DayComponent } from './advanced-prediction/predicted-city/day/day.component';
import { LoadingDannyComponent } from './loading-danny/loading-danny.component';

@NgModule({
  declarations: [AppComponent, SimplePredictionComponent, CardComponent, WelcomeScreenComponent, CitiesComponent, CityComponent, CitySelectionComponent, WeatherComponent, PredictedCityComponent, DayComponent, LoadingDannyComponent],
  imports: [BrowserModule, AppRoutingModule, FormsModule, HttpClientModule],
  providers: [],
  bootstrap: [AppComponent],
})
export class AppModule {}
