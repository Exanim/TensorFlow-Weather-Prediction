export interface WeatherAPIResponse {
  coord: Coord;
  weather: Weather[];
  base: string;
  main: Main;
  visibility: number;
  wind: Wind;
  rain: Rain;
  clouds: Clouds;
  dt: number;
  sys: Sys;
  timezone: number;
  id: number;
  name: string;
  cod: number;
}

export interface DayData {
  cityName: string;
  day: Day[];
}

export interface Day {
  temperature: number;
  humidity: number;
  name?: string;
}

export interface CustomBackendData {
  today: Today;
  next_week: NextWeek;
  next_month: NextMonth;
  next_year: NextYear;
}

export interface Today {
  temperature: number;
  humidity: number;
  name?: string;
}

export interface NextWeek {
  temperature: number;
  humidity: number;
  name?: string;
}

export interface NextMonth {
  temperature: number;
  humidity: number;
  name?: string;
}

export interface NextYear {
  temperature: number;
  humidity: number;
  name?: string;
}

export interface GeoAPIResponse {
  name: string;
  local_names: string[];
  lat: number;
  lon: number;
  country: string;
}

export interface Coord {
  lon: number;
  lat: number;
}

export interface Weather {
  id: number;
  main: string;
  description: string;
  icon: string;
}

export interface Main {
  temp: number;
  feels_like: number;
  temp_min: number;
  temp_max: number;
  pressure: number;
  humidity: number;
  sea_level: number;
  grnd_level: number;
}

export interface Wind {
  speed: number;
  deg: number;
  gust: number;
}

export interface Rain {
  '1h': number;
}

export interface Clouds {
  all: number;
}

export interface Sys {
  type: number;
  id: number;
  country: string;
  sunrise: number;
  sunset: number;
}
