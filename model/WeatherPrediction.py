import json
import logging
import os
import asyncio
import datetime
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

import csv_cleaner
import numpy as np
import tensorflow as tf
from sklearn.preprocessing import StandardScaler
from output_transform import chaotic_randomizer
from output_transform.global_warming_rate import logarithmic_warming_rate


hostname = "localhost"
port = 8000
title = "TensorFlow-Weather-API"
default_cities =["budapest", "szeged", "nyiregyhaza", "sopron"]


class WeatherPrediction:
    def __init__(self, city):
        self.city = city.lower()
        self.file_path = os.path.join('csv_data', f'{city}_data.csv')
        self.df = csv_cleaner.replace_hiány_with_mean(os.path.join('csv_data', f'{city}_data.csv'))
        self.scaler = StandardScaler()
        self.df[['temperature', 'total_rainfall']] = self.scaler.fit_transform(
            self.df[['temperature', 'total_rainfall']])
        self.model_path = f'models/year_ignore_{city}_model.keras'
        self.loaded_model = tf.keras.models.load_model(self.model_path)

    async def process_date(self, date):
        new_data = np.array([[date.month, date.day]])
        predictions = self.scaler.inverse_transform(self.loaded_model.predict(new_data))

        temperature = logarithmic_warming_rate(date.year, predictions[0, 0])
        rain = chaotic_randomizer.chaotic_random()

        return [temperature, rain]

    async def predict_weather_async(self, start_date, end_date):
        pred_list = []

        current_date = start_date
        delta = datetime.timedelta(days=1)
        tasks = []

        while current_date <= end_date:
            tasks.append(self.process_date(current_date))
            current_date += delta

        results = await asyncio.gather(*tasks)
        pred_list.extend(results)

        return pred_list


async def get_weather_data(date: datetime, city):
    city = city.lower()
    weather_predictor = WeatherPrediction(city)
    task = asyncio.create_task(weather_predictor.process_date(date))
    return await task


class WeatherApi(BaseHTTPRequestHandler):
    def do_GET(self):
        logging.info("GET STARTED")

        parsed_path = urlparse(self.path)
        query_params = parse_qs(parsed_path.query)

        if query_params.get('city', [None])[0] is None:
            city = "szeged"
        elif query_params.get('city', [None])[0].lower() not in default_cities:
            self.send_response(404)
            """
            self.send_header("Content-type", "application/json")
            self.end_headers()
            response_data = {
                "city not found": query_params.get('city', [None])[0], # I leave this here, just in case
            }
            response_json = json.dumps(response_data)
            self.wfile.write(bytes(response_json, "utf-8"))
            """
            return
        else:
            city = query_params.get('city', [None])[0]

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
