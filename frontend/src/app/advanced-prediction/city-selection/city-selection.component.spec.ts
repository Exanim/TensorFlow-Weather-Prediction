import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CitySelectionComponent } from './city-selection.component';

describe('CitySelectionComponent', () => {
  let component: CitySelectionComponent;
  let fixture: ComponentFixture<CitySelectionComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ CitySelectionComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(CitySelectionComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
