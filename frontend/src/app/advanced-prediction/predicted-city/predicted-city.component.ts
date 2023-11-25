import { Component, OnInit, inject } from '@angular/core';
import { DataStorageService } from '../weather/shared/data-storage.service';
import { ActivatedRoute } from '@angular/router';
import { Subscription } from 'rxjs';
import {
  CustomBackendData,
  DayData,
} from '../weather/shared/get-all-request.model';

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
  understandableCity?: DayData;

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
          if (this.city) {
            this.understandableCity = {
              cityName: this.city,
              day: [
                {
                  temperature: this.daysData.today.temperature,
                  humidity: this.daysData.today.humidity,
                  name: this.daysData.today.name,
                },
                {
                  temperature: this.daysData.next_week.temperature,
                  humidity: this.daysData.next_week.humidity,
                  name: this.daysData.next_week.name,
                },
                {
                  temperature: this.daysData.next_month.temperature,
                  humidity: this.daysData.next_month.humidity,
                  name: this.daysData.next_month.name,
                },
                {
                  temperature: this.daysData.next_year.temperature,
                  humidity: this.daysData.next_year.humidity,
                  name: this.daysData.next_year.name,
                },
              ],
            };
          }
          console.log(this.understandableCity);
          this.isLoading = false;
        });
    }, 500);
  }

  ngOnDestroy() {
    this.routeSubscription.unsubscribe();
    this.dataSubscription.unsubscribe();
  }
}
