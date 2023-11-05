export class Weather {
  constructor(
    public dt_txt: string,
    public temp: number,
    public humidity: number,
    public weather: string,
    public windSpeed: number
  ) {}
}
