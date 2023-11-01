import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { SimplePredictionComponent } from './simple-prediction/simple-prediction.component';
import { FormsModule } from '@angular/forms';
import { CardComponent } from './simple-prediction/card/card.component';

@NgModule({
  declarations: [AppComponent, SimplePredictionComponent, CardComponent],
  imports: [BrowserModule, AppRoutingModule, FormsModule],
  providers: [],
  bootstrap: [AppComponent],
})
export class AppModule {}
