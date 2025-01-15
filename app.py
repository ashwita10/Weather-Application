import requests
import tkinter as tk
from tkinter import messagebox
import os
os.environ["TCL_LIBRARY"] = "C:/Users/ashwita/AppData/Local/Programs/Python/Python313/tcl/tcl8.6"
os.environ["TK_LIBRARY"] = "C:/Users/ashwita/AppData/Local/Programs/Python/Python313/tcl/tk8.6"

# Function to fetch weather data from OpenWeatherMap API
def get_weather(city):
    API_KEY = "YOUR_API_KEY"  # Replace with your OpenWeatherMap API key
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

    try:
        response = requests.get(BASE_URL, params={"q": city, "appid": API_KEY, "units": "metric"})
        response.raise_for_status()
        weather_data = response.json()

        if weather_data["cod"] != 200:
            raise ValueError(weather_data.get("message", "Error fetching weather data."))

        return {
            "city": weather_data["name"],
            "temperature": weather_data["main"]["temp"],
            "description": weather_data["weather"][0]["description"].capitalize(),
            "humidity": weather_data["main"]["humidity"],
            "wind_speed": weather_data["wind"]["speed"],
        }

    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Network error: {e}")
    except ValueError as e:
        messagebox.showerror("Error", str(e))

# Function to display weather data in the GUI
def display_weather():
    city = city_entry.get()

    if not city:
        messagebox.showwarning("Input Required", "Please enter a city name.")
        return

    weather = get_weather(city)

    if weather:
        result_label.config(text=f"City: {weather['city']}\n"
                               f"Temperature: {weather['temperature']}°C\n"
                               f"Description: {weather['description']}\n"
                               f"Humidity: {weather['humidity']}%\n"
                               f"Wind Speed: {weather['wind_speed']} m/s")

# Initialize the Tkinter GUI application
app = tk.Tk()
app.title("Weather Application")
app.geometry("400x300")

# GUI components
city_label = tk.Label(app, text="Enter City:")
city_label.pack(pady=10)

city_entry = tk.Entry(app, width=30)
city_entry.pack(pady=5)

search_button = tk.Button(app, text="Get Weather", command=display_weather)
search_button.pack(pady=10)

result_label = tk.Label(app, text="", justify="left", font=("Arial", 12))
result_label.pack(pady=20)

# Run the application
app.mainloop()
