import { Component, OnInit, inject } from '@angular/core';
import { DataStorageService } from '../weather/shared/data-storage.service';

@Component({
  selector: 'app-predicted-city',
  templateUrl: './predicted-city.component.html',
  styleUrls: ['./predicted-city.component.css'],
})
export class PredictedCityComponent implements OnInit {
  private http = inject(DataStorageService);

  ngOnInit(): void {
    this.http.getTensorFlowData().subscribe((data) => {
      console.log(data);
    });
  }
}
