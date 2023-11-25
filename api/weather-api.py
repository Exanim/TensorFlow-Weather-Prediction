import json
import logging
import asyncio
import datetime
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
from model.WeatherPrediction import get_weather_data

hostname = "localhost"
port = 8000
title = "TensorFlow-Weather-API"
default_cities = ["budapest", "szeged", "nyiregyhaza", "sopron"]


class WeatherApi(BaseHTTPRequestHandler):

    def do_GET(self):

        path = self.path
        endpoint_name = path.strip('/').replace('/', '_')
        method_name = f'do_GET_{endpoint_name}'

        if path == "/":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            response = {"message": "Welcome to the Weather API!"}
            self.wfile.write(json.dumps(response).encode())
            return


        parsed_path = urlparse(self.path)
        query_params = parse_qs(parsed_path.query)
        city = query_params.get('city', default_cities)[0].lower()

        if city not in default_cities:
            self.send_response(404)
            return
        else:
            self.do_GET_city(city)

        if hasattr(self, method_name):
            getattr(self, method_name)()
        else:
            # Handle unknown paths with a 404 response
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write("Not Found".encode())

    def do_GET_forecast(self):
        # Custom endpoint for the path "/forecast"
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        response = {"message": "Weather forecast for the next week"}
        self.wfile.write(json.dumps(response).encode())

    def do_GET_city(self, city):
        logging.info("GET STARTED")

        data = []
        today = datetime.date.today()
        next_week = datetime.date.today() + datetime.timedelta(days=7)
        next_month = datetime.date.today() + datetime.timedelta(days=30)
        next_year = datetime.date.today() + datetime.timedelta(days=365)
        # next_decade = datetime.date.today() + datetime.timedelta(days=365 * 10)

        data.append(asyncio.run(get_weather_data(today, city)))
        data.append(asyncio.run(get_weather_data(next_week, city)))
        data.append(asyncio.run(get_weather_data(next_month, city)))
        data.append(asyncio.run(get_weather_data(next_year, city)))

        print(data)

        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()

        response_data = {
            "city": city,
            "today": {
                "temperature": data[0][0],
                "total_rain": data[0][1],
            },
            "next_week": {
                "temperature": data[1][0],
                "total_rain": data[1][1],
            },
            "next_month": {
                "temperature": data[2][0],
                "total_rain": data[2][1],
            },
            "next_year": {
                "temperature": data[3][0],
                "total_rain": data[3][1],
            }
        }

        response_json = json.dumps(response_data)
        self.wfile.write(bytes(response_json, "utf-8"))


if __name__ == "__main__":
    """
    city = "Budapest"
    weather_predictor = WeatherPrediction(city)
    start_date = datetime.date(2500, 1, 1)
    end_date = datetime.date(2500, 1, 1)

    loop = asyncio.get_event_loop()
    prediction_list = loop.run_until_complete(weather_predictor.predict_weather_async(start_date, end_date))
    loop.close()
    print(prediction_list)
    """
    webServer = HTTPServer((hostname, port), WeatherApi)
    print("Server started http://%s:%s" % (hostname, port))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
