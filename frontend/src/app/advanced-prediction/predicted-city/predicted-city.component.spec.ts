import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PredictedCityComponent } from './predicted-city.component';

describe('PredictedCityComponent', () => {
  let component: PredictedCityComponent;
  let fixture: ComponentFixture<PredictedCityComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ PredictedCityComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(PredictedCityComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
