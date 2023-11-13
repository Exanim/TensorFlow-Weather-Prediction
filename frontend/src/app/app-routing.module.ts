import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { SimplePredictionComponent } from './simple-prediction/simple-prediction.component';
import { WelcomeScreenComponent } from './welcome-screen/welcome-screen.component';
import { CitySelectionComponent } from './advanced-prediction/city-selection/city-selection.component';
import { WeatherComponent } from './advanced-prediction//weather/weather.component';
import { CitiesComponent } from './advanced-prediction/cities/cities.component';

const routes: Routes = [
  { path: '', redirectTo: '/welcome', pathMatch: 'full' },
  { path: 'welcome', component: WelcomeScreenComponent },
  { path: 'weather', component: SimplePredictionComponent },
  { path: 'tensor', component: CitiesComponent},
  { path: 'city-selection', component: CitySelectionComponent },
  { path: 'weather/:city', component: WeatherComponent },
  { path: '', redirectTo: '/city-selection', pathMatch: 'full' },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}
