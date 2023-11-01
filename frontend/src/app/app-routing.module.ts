import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { SimplePredictionComponent } from './simple-prediction/simple-prediction.component';

const routes: Routes = [
  { path: 'weather', component: SimplePredictionComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}
