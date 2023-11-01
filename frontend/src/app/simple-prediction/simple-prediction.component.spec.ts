import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SimplePredictionComponent } from './simple-prediction.component';

describe('SimplePredictionComponent', () => {
  let component: SimplePredictionComponent;
  let fixture: ComponentFixture<SimplePredictionComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ SimplePredictionComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(SimplePredictionComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
