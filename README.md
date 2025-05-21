# FreeWeatherApp
This Python code creates a simple desktop weather application using the PyQt5 library for the graphical user interface (GUI) and the OpenWeatherMap API to fetch weather data.

Purpose:
The application allows users to input a city name and retrieve current weather information (temperature, weather description, humidity, and wind speed) for that city.
The data is fetched from the OpenWeatherMap API and displayed in a GUI window.

GUI Setup:
Uses PyQt5 to create a window with a text input field for the city name, a "Get Weather" button, and a label to display the weather information.
The window is titled "Weather Forecast" and has a fixed size (400x200 pixels).

API Integration:
Makes an HTTP request to the OpenWeatherMap API to retrieve weather data for a specified city.
Displays the results in metric units (e.g., temperature in Celsius, wind speed in meters per second).

Error Handling:
Validates user input (checks if the city name is empty).
Handles API errors (e.g., invalid city name or network issues) and displays user-friendly error messages.

Workflow:
The user enters a city name in the text field.
Clicking the "Get Weather" button triggers an API call to fetch weather data.
The app displays the weather details (city, temperature, weather description, humidity, wind speed) or an error message if the request fails.

Output:
If successful, the app shows formatted weather information in the GUI.
If the city is invalid or an error occurs, a pop-up message (warning or critical) informs the user.
