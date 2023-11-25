import { Component, OnInit, inject } from '@angular/core';
import { DataStorageService } from '../weather/shared/data-storage.service';
import { ActivatedRoute } from '@angular/router';
import { Subscription } from 'rxjs';
import { CustomBackendData } from '../weather/shared/get-all-request.model';

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
  daysData?: CustomBackendData;
  isLoading = true;

  ngOnInit(): void {
    this.routeSubscription = this.route.params.subscribe((params) => {
      this.city = params['city'];
    });
    setTimeout(() => {
      this.dataSubscription = this.http
        .getTensorFlowData(this.city)
        .subscribe((data) => {
          this.daysData = data;
          this.daysData.today.name = this.days[0];
          this.daysData.next_week.name = this.days[1];
          this.daysData.next_month.name = this.days[2];
          this.daysData.next_year.name = this.days[3];
          console.log(this.daysData);
          this.isLoading = false;
        });
    }, 500);
  }

  ngOnDestroy() {
    this.routeSubscription.unsubscribe();
    this.dataSubscription.unsubscribe();
  }
}
