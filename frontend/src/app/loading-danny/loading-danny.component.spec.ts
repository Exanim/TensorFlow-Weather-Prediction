import { ComponentFixture, TestBed } from '@angular/core/testing';

import { LoadingDannyComponent } from './loading-danny.component';

describe('LoadingDannyComponent', () => {
  let component: LoadingDannyComponent;
  let fixture: ComponentFixture<LoadingDannyComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ LoadingDannyComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(LoadingDannyComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
