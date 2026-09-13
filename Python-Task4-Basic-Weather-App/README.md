# Basic Weather App

## Description

A simple Python-based weather application that fetches current weather information using the OpenWeatherMap API.

The user enters a city name or ZIP code, and the application displays temperature, humidity, weather condition, and wind speed.

## Features

- Accepts city name or ZIP code
- Fetches real-time weather information
- Displays temperature in Celsius
- Displays humidity percentage
- Displays weather condition
- Displays wind speed
- Handles invalid city names
- Handles network errors
- Validates empty input
- Keeps API key secure using a `.env` file

## Technologies Used

- Python
- Requests
- OpenWeatherMap API
- python-dotenv

## How to Run

1. Install the required libraries:

```bash
pip install requests python-dotenv