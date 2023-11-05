import { ComponentFixture, TestBed } from '@angular/core/testing';
import { CardComponent } from './card.component';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { By } from '@angular/platform-browser';

describe('Component: App', () => {
  let fixture: ComponentFixture<CardComponent>;
  let app: CardComponent;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [CardComponent],
      imports: [FormsModule, HttpClientModule],
    }).compileComponents();
    fixture = TestBed.createComponent(CardComponent);
    app = fixture.componentInstance;
  });

  it('should create the app', () => {
    expect(app).toBeTruthy();
  });

  it('should have a definition of card', () => {
    expect(app.card).toBeDefined();
  });

  it('should have .day class', () => {
    const el = fixture.debugElement.query(By.css('.day'));
    expect(el).toBeTruthy();
  })

  it('should have an img tag', () => {
    const el = fixture.debugElement.query(By.css('img'));
    expect(el).toBeTruthy();
  })

  it('should have an .temp tag', () => {
    const el = fixture.debugElement.query(By.css('.temp'));
    expect(el).toBeTruthy();
  })

  it('should have an .details tag', () => {
    const el = fixture.debugElement.query(By.css('.details'));
    expect(el).toBeTruthy();
  })

  it('should have an .details .col tag', () => {
    const el = fixture.debugElement.query(By.css('.details .col'));
    expect(el).toBeTruthy();
  })

  it('should have an .details tag with .col tag and div element', () => {
    const el = fixture.debugElement.query(By.css('.details .col div'));
    expect(el).toBeTruthy();
  })

  it('should have an .details tag with .col tag and div element and svg element', () => {
    const el = fixture.debugElement.query(By.css('.details .col div svg'));
    expect(el).toBeTruthy();
  })

  it('should have an .details tag with .col tag, div element, svg element and path element', () => {
    const el = fixture.debugElement.query(By.css('.details .col div svg path'));
    expect(el).toBeTruthy();
  })

  it('should have an .details tag with .col tag, div element and .humidity', () => {
    const el = fixture.debugElement.query(By.css('.details .col div .humidity'));
    expect(el).toBeTruthy();
  })

  it('should have an .details tag with .col tag, div element and p element', () => {
    const el = fixture.debugElement.query(By.css('.details .col div p'));
    expect(el).toBeTruthy();
  })

  it('should have an .details tag with .col tag, div element and .wind', () => {
    const el = fixture.debugElement.query(By.css('.details .col div .wind'));
    expect(el).toBeTruthy();
  })

  it('should have an .details tag with .col tag, div element and p element with "0%"', () => {
    fixture.detectChanges();
    const el = fixture.debugElement.query(By.css('.details .col div p'));
    const pText = el.nativeElement.textContent;
    expect(pText).toContain('0%');
  })

  it('should have an .details tag with .col tag, div element and p element with "Páratartalom"', () => {
    fixture.detectChanges();
    const pElements = fixture.debugElement.queryAll(By.css('.details .col p')); // Keresd meg az összes <p> elemet
    const pText = pElements[1].nativeElement.textContent;
    expect(pText).toContain('Páratartalom');
  })

  it('should have an .details tag with .col tag, div element and p element with "0km/h"', () => {
    fixture.detectChanges();
    const pElements = fixture.debugElement.queryAll(By.css('.details .col p')); // Keresd meg az összes <p> elemet
    const pText = pElements[2].nativeElement.textContent;
    expect(pText).toContain('0.0 km/h');
  })

  it('should have an .details tag with .col tag, div element and p element with "Szélsebesség"', () => {
    fixture.detectChanges();
    const pElements = fixture.debugElement.queryAll(By.css('.details .col p')); // Keresd meg az összes <p> elemet
    const pText = pElements[3].nativeElement.textContent;
    expect(pText).toContain('Szélsebesség');
  })
});
