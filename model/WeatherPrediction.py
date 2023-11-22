import json
import logging
import os
import asyncio
import datetime
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

import csv_cleaner
import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn.preprocessing import StandardScaler
from output_transform import chaotic_randomizer
from output_transform.global_warming_rate import logarithmic_warming_rate


hostname = "localhost"
port = 8000

title = "TensorFlow-Weather-API"


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


async def get_weather_data():
    weather_predictor = WeatherPrediction("Budapest")
    task = asyncio.create_task(weather_predictor.process_date(datetime.date.today()))
    return await task


class WeatherApi(BaseHTTPRequestHandler):
    def do_GET(self):
        logging.info("GET STARTED")

        data = asyncio.run(get_weather_data())
        print(data)

        parsed_path = urlparse(self.path)
        query_params = parse_qs(parsed_path.query)

        if not query_params.get('param1',[None])[0] is None:
            foo = query_params.get('param1',[None])[0]

        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()

        response_data = {
            "temperature": data[0],
            "humidity": data[1],
        }

        response_json = json.dumps(response_data)
        self.wfile.write(bytes(response_json, "utf-8"))


# Example usage:
if __name__ == "__main__":
    # city = "Budapest"
    # weather_predictor = WeatherPrediction(city)
    # start_date = datetime.date(2500, 1, 1)
    # end_date = datetime.date(2500, 1, 1)
    #
    # # Use async event loop
    # loop = asyncio.get_event_loop()
    # prediction_list = loop.run_until_complete(weather_predictor.predict_weather_async(start_date, end_date))
    # loop.close()
    # print(prediction_list)
    webServer = HTTPServer((hostname, port), WeatherApi)
    print("Server started http://%s:%s" % (hostname, port))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
    # print(asyncio.run(get_weather_data()))
