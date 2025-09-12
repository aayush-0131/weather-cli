# Weather CLI 🌦️

A simple command-line tool to get the current weather for any city.

Built in Python, this project uses the [OpenWeatherMap API](https://openweathermap.org/api) to fetch real-time weather data. It also demonstrates the use of a `.env` file to securely manage API keys.

## Setup & Usage

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/weather-cli.git](https://github.com/your-username/weather-cli.git)
    cd weather-cli
    ```

2.  **Create a virtual environment and install dependencies:**
    ```bash
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```
    *(Note: We will create the `requirements.txt` file in the next step).*

3.  **Create your secrets file:**
    This project requires a free API key from OpenWeatherMap.
    * Create a file named `.env` in the root of the project.
    * Add your API key to it like this:
        ```
        OPENWEATHER_API_KEY="your_secret_api_key_here"
        ```

4.  **Run the application:**
    ```bash
    python weather_cli.py
    ```
    The program will then prompt you to enter a city name.