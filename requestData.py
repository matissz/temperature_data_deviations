import yr_weather

sitename  = {
    "GitHub":"matissz"
}
headers = {
    "User-Agent": "matiss.zigalvis@gmail.com"
}


def main():
    my_client = yr_weather.Locationforecast(headers=headers)


    air_temp = my_client.get_air_temperature(56.94, 24.10)
    forcast = my_client.get_forecast(56.94, 24.10)
    
    timeseries_list = forcast._timeseries



    for item in timeseries_list:
        for key, value in item.items():
            if key == "time":
                print()
                print(f"{key}: {value}")    
            if key == "data":
                    for data_key, data_item  in value.items():
                        if data_key == "instant":
                            for instant_key, instant_item in data_item.items():
                                if instant_key == "details":
                                    for details_key, details_item in instant_item.items():
                                        if details_key == "air_temperature":
                                            print(f"{details_key} : {details_item} | current temp:{air_temp} | deviation {details_item - air_temp:.2f} ")





if __name__ == "__main__":
    main()