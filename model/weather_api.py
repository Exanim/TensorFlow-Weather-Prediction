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


def city_in_default_cities(city):
    return city in default_cities


def get_last_path_element(path):
    return path.split('/')[-1]


class WeatherApi(BaseHTTPRequestHandler):

    def do_GET(self):
        logging.info("GET STARTED")

        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            response = {"message": "Welcome to the Weather API!"}
            self.wfile.write(json.dumps(response).encode())
            return

        city = get_last_path_element(self.path)
        if not city_in_default_cities(city):
            self.send_response(404)
            return
        print(city)

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

        self.send_header("Access-Control-Allow-Origin", "http://localhost:4200")
        self.send_header("Access-Control-Allow-Methods", "GET")
        self.send_header("Access-Control-Allow-Headers", "Content-type")

        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()

        response_data = {
            "city": city,
            "today": {
                "temperature": data[0][0],
                "humidity": data[0][1],
            },
            "next_week": {
                "temperature": data[1][0],
                "humidity": data[1][1],
            },
            "next_month": {
                "temperature": data[2][0],
                "humidity": data[2][1],
            },
            "next_year": {
                "temperature": data[3][0],
                "humidity": data[3][1],
            }
        }

        response_json = json.dumps(response_data)
        self.wfile.write(bytes(response_json, "utf-8"))


if __name__ == "__main__":
    webServer = HTTPServer((hostname, port), WeatherApi)
    print("Server started http://%s:%s" % (hostname, port))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
