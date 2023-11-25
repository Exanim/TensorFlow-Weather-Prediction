import { Component, OnInit, inject } from '@angular/core';
import { DataStorageService } from '../weather/shared/data-storage.service';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-predicted-city',
  templateUrl: './predicted-city.component.html',
  styleUrls: ['./predicted-city.component.css'],
})
export class PredictedCityComponent implements OnInit {
  private http = inject(DataStorageService);
  private route = inject(ActivatedRoute);
  city?: string;
  isLoading = true;

  ngOnInit(): void {
    this.route.params.subscribe((params) => {
      this.city = params['city'];
    });
    this.http.getTensorFlowData(this.city).subscribe((data) => {
      console.log(data);
      this.isLoading = false;
    });
  }
}
