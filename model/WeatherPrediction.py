import os
import asyncio
import datetime

import numpy as np
import tensorflow as tf
from sklearn.preprocessing import StandardScaler

from model import csv_cleaner
from model.output_transform import chaotic_randomizer
from model.output_transform.global_warming_rate import logarithmic_warming_rate


class WeatherPrediction:
    def __init__(self, city_name):
        self.city = city_name.lower()
        self.file_path = os.path.join('csv_data', f'{city_name}_data.csv')
        self.df = csv_cleaner.replace_missing_values(os.path.join('csv_data', f'{city_name}_data.csv'))
        self.scaler = StandardScaler()
        self.df[['temperature', 'total_rainfall']] = self.scaler.fit_transform(
            self.df[['temperature', 'total_rainfall']])
        self.model_path = f'models/year_ignore_{city_name}_model.keras'
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


if __name__ == "__main__":
    city = "Budapest"
    weather_predictor = WeatherPrediction(city)
    start_date = datetime.date(2500, 1, 1)
    end_date = datetime.date(2500, 1, 1)

    loop = asyncio.get_event_loop()
    prediction_list = loop.run_until_complete(weather_predictor.predict_weather_async(start_date, end_date))
    loop.close()
    print(prediction_list)
