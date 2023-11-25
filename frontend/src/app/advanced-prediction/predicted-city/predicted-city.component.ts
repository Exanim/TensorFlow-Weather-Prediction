import { Component, OnInit, inject } from '@angular/core';
import { DataStorageService } from '../weather/shared/data-storage.service';
import { ActivatedRoute } from '@angular/router';
import { Subscription } from 'rxjs';

@Component({
  selector: 'app-predicted-city',
  templateUrl: './predicted-city.component.html',
  styleUrls: ['./predicted-city.component.css'],
})
export class PredictedCityComponent implements OnInit {
  private http = inject(DataStorageService);
  private route = inject(ActivatedRoute);
  routeSubscription = new Subscription();
  dataSubscription = new Subscription();
  city?: string;
  days = ['Ma', 'Jövőhét', 'Jövő hónap', 'Jövő év'];
  isLoading = true;

  ngOnInit(): void {
    this.routeSubscription = this.route.params.subscribe((params) => {
      this.city = params['city'];
    });
    setTimeout(() => {
      this.dataSubscription = this.http
        .getTensorFlowData(this.city)
        .subscribe((data) => {
          this.isLoading = false;
          console.log(data);
        });
    }, 500);
  }

  ngOnDestroy() {
    this.routeSubscription.unsubscribe();
    this.dataSubscription.unsubscribe();
  }
}
