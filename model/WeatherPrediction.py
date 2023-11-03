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

    


# Example usage:
if __name__ == "__main__":
    city = "budapest"  # lowercase
    weather_predictor = WeatherPrediction(city)
    start_date = datetime.date(2500, 11, 1)
    end_date = datetime.date(2502, 1, 1)
    print(weather_predictor.predict_weather(start_date, end_date))
