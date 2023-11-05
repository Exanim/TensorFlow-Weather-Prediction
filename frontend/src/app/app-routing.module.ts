import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { SimplePredictionComponent } from './simple-prediction/simple-prediction.component';
import { WelcomeScreenComponent } from './welcome-screen/welcome-screen.component';

const routes: Routes = [
  { path: '', redirectTo: '/welcome', pathMatch: 'full' },
  { path: 'welcome', component: WelcomeScreenComponent },
  { path: 'weather', component: SimplePredictionComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}
