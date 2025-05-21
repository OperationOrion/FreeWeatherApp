# -*- coding: utf-8 -*-
"""
Mitchell McLaughlin
Weather App FREE!
12/20/24
"""

import sys
import requests
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QLabel, QLineEdit, QPushButton, QWidget, QMessageBox
)
import os

class WeatherApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Weather Forecast")
        self.setGeometry(300, 300, 400, 200)

        self.api_key = os.getenv("OPENWEATHER_API_KEY", "your-api-key-here")  # Replace with your API key or use env variable

        # Main Widget
        main_widget = QWidget()
        self.setCentralWidget(main_widget)

        # Layout
        layout = QVBoxLayout()

        # City Input
        self.city_label = QLabel("Enter City Name:")
        layout.addWidget(self.city_label)

        self.city_input = QLineEdit()
        layout.addWidget(self.city_input)

        # Fetch Button
        self.fetch_button = QPushButton("Get Weather")
        self.fetch_button.clicked.connect(self.get_weather)
        layout.addWidget(self.fetch_button)

        # Weather Display
        self.weather_result = QLabel("")
        self.weather_result.setStyleSheet("font-size: 16px;")
        layout.addWidget(self.weather_result)

        main_widget.setLayout(layout)

    def get_weather(self):
        city = self.city_input.text().strip()
        if not city:
            QMessageBox.warning(self, "Input Error", "Please enter a city name.")
            return

        self.fetch_button.setEnabled(False)
        self.weather_result.setText("Fetching weather...")
        QApplication.processEvents()

        try:
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.api_key}&units=metric"
            response = requests.get(url)
            data = response.json()

            if response.status_code == 200:
                if "main" in data and "weather" in data and "wind" in data:
                    temp_celsius = data["main"]["temp"]
                    temp_fahrenheit = temp_celsius * 9/5 + 32  # Convert to Fahrenheit
                    weather_desc = data["weather"][0]["description"]
                    humidity = data["main"]["humidity"]
                    wind_speed = data["wind"]["speed"]

                    result = (
                        f"City: {city}\n"
                        f"Temperature: {temp_celsius}°C\n"
                        f"Temperature: {temp_fahrenheit:.1f}°F\n"
                        f"Weather: {weather_desc}\n"
                        f"Humidity: {humidity}%\n"
                        f"Wind Speed: {wind_speed} m/s"
                    )
                    self.weather_result.setText(result)
                else:
                    QMessageBox.warning(self, "Error", "Unexpected API response format.")
            else:
                QMessageBox.warning(self, "Error", data.get("message", "Could not fetch weather data."))
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Error", f"Network error: {str(e)}")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred: {str(e)}")
        finally:
            self.fetch_button.setEnabled(True)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WeatherApp()
    window.show()
    sys.exit(app.exec_())