export class Card {
  constructor(
    public day: string,
    public imgSrc: string,
    public temperature: number,
    public temperatureType: boolean,
    public humidity: number,
    public windSpeed: number
  ) {}
}
