import yr_weather
from forcast import get_forcastData

def main():
    temp_now()
    check_temperature()


def temp_now() -> float:
    headers = {"User-Agent": "matiss.zigalvis@gmail.com"}
    my_client = yr_weather.Locationforecast(headers=headers)

    air_temp = my_client.get_air_temperature(56.94, 24.10)

    return air_temp


def check_temperature():
    future_forcast =  get_forcastData()
    current_temp = temp_now()

    print(f"Current temperateure: {current_temp}")

    for unique_id, data in future_forcast.items():
        forecast_time = data["time "]
        forecast_temp = data["air_temperature"]
        print(f"Forecast Time: {forecast_time}, Forecast Temperature: {forecast_temp}")
        print(f"Deviation from Forecast: {forecast_temp - current_temp:.1f}")




if __name__ == "__main__":
    main()