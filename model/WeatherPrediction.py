import os
import datetime
import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn.preprocessing import StandardScaler
from output_transform import chaotic_randomizer
from output_transform.global_warming_rate import logarithmic_warming_rate


class WeatherPrediction:
    def __init__(self, city):
        self.city = city.lower()
        self.file_path = os.path.join('csv_data', f'{city}_data.csv')
        self.df = pd.read_csv(self.file_path)
        self.df.fillna(self.df.mean(), inplace=True)
        self.scaler = StandardScaler()
        self.df[['temperature', 'total_rainfall']] = self.scaler.fit_transform(
            self.df[['temperature', 'total_rainfall']])
        self.model_path = f'models/year_ignore_{city}_model.keras'
        self.loaded_model = tf.keras.models.load_model(self.model_path)

    def predict_weather(self, start_date, end_date):
        current_date = start_date
        delta = datetime.timedelta(days=1)
        pred_list = []

        while current_date <= end_date:
            new_data = np.array([[current_date.month, current_date.day]])
            predictions = self.scaler.inverse_transform(self.loaded_model.predict(new_data))

            temperature = logarithmic_warming_rate(current_date.year, predictions[0, 0])
            rain = chaotic_randomizer.chaotic_random()

            pred_list.append([temperature, rain])

            current_date += delta
        return pred_list


# Example usage:
if __name__ == "__main__":
    city = "budapest"  # lowercase
    weather_predictor = WeatherPrediction(city)
    start_date = datetime.date(2500, 11, 1)
    end_date = datetime.date(2502, 1, 1)
    print(weather_predictor.predict_weather(start_date, end_date))
