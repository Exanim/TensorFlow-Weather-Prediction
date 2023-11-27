import datetime
import os
import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

from model.csv_cleaner import replace_missing_values
from model.output_transform import chaotic_randomizer
from model.output_transform.global_warming_rate import logarithmic_warming_rate

file_path = os.path.join('../csv_data', 'szeged_data.csv')
df = pd.read_csv(file_path)

df_replaced = replace_missing_values(file_path)
df = df_replaced

scaler = StandardScaler()
df[['temperature', 'total_rainfall']] = scaler.fit_transform(df[['temperature', 'total_rainfall']])

# Modify X to include only "month" and "day" features
X = df[['month', 'day']]
y = df[['temperature', 'total_rainfall']]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(2,)),  # Input layer with 2 features (month and day)
    tf.keras.layers.Dense(64),
    tf.keras.layers.PReLU(),
    tf.keras.layers.Dense(64),
    tf.keras.layers.PReLU(),
    tf.keras.layers.Dense(2)  # Output layer with 2 features (temperature and rain)
])

# Compile the model
model.compile(optimizer='adam', loss='mean_squared_error')

# Train the model
model.fit(X_train, y_train, epochs=40, batch_size=64, validation_data=(X_test, y_test))

# Evaluate the model on the test data
loss = model.evaluate(X_test, y_test)

model.save('year_ignore_szeged_model.keras')

start_date = datetime.date(2500, 11, 1)
end_date = datetime.date(2502, 1, 1)
delta = datetime.timedelta(days=1)

current_date = start_date
while current_date <= end_date:
    new_data = np.array([[current_date.month, current_date.day]])
    predictions = scaler.inverse_transform(model.predict(new_data))

    temperature = logarithmic_warming_rate(current_date.year, predictions[0, 0])
    rain = chaotic_randomizer.chaotic_random()

    print(f"Date: {current_date}, Predicted temperature: {predictions[0, 0]}, Predicted total rainfall: {rain}")

    current_date += delta
