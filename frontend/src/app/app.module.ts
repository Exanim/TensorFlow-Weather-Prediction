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

@NgModule({
  declarations: [AppComponent, SimplePredictionComponent, CardComponent, WelcomeScreenComponent, CitiesComponent],
  imports: [BrowserModule, AppRoutingModule, FormsModule, HttpClientModule],
  providers: [],
  bootstrap: [AppComponent],
})
export class AppModule {}
