import yr_weather
import datetime

headers = {"User-Agent": "matiss.zigalvis@gmail.com"}


def main():
    my_client = yr_weather.Locationforecast(headers=headers)

    air_temp = my_client.get_air_temperature(56.94, 24.10)
    forcast = my_client.get_forecast(56.94, 24.10)

    timeseries_list = forcast._timeseries

    forcastDic = {"datetime": "", "air_temperature": ""}

    # select only next three days, as they have forcast for each hour
    # current day + 2

    # create new dictionalry wiht values key as date, value as air_temperature
    # create seperate new dict that colects current temp reading and stores key as date, value as  current temp

    # create deviations output where if defiation is bigger than 2 degrees marke deviation value in read color

    # create schedual job to get current temp vale each hour and store the valuw in above seperate dictionalry

    # sepreat the code - get currnet temp readigng / - get forcast reading  / - scheduele temp update / - print deviation values

    # if currnet temp is below 7 degrees ask user to adjust the heating!

    # when defining custom fuction add docustring
    

    for item in timeseries_list:
        currnetDay = None
        dayAfterTomorrow = None
        
        for key, value in item.items():
            
            if key == "time":                
            # datetime manipulation to process only next three days
                datetimeObj = datetime.datetime.strptime(value, "%Y-%m-%dT%H:%M:%SZ")  # vlaue contians time value, that is str, have to adjust the time format | update: clean up datetime str
                currnetDay = datetimeObj.date()

                
            if dayAfterTomorrow is None:
                dayAfterTomorrow = currnetDay + datetime.timedelta(days=1)
                
            ##datetime manipulation end            
                        
            if currnetDay <= dayAfterTomorrow and key =="time":
                print()     
                print(f"{key}: {datetimeObj}") 
                        
            if currnetDay <= dayAfterTomorrow and key == "data":
                    for data_key, data_item in value.items():
                        if data_key == "instant":
                            for instant_key, instant_item in data_item.items():
                                if instant_key == "details":
                                    for (details_key, details_item) in instant_item.items():
                                        if details_key == "air_temperature":
                                            print(f"{details_key} : {details_item} | current temp:{air_temp} | deviation {details_item - air_temp:.1f}")
            


if __name__ == "__main__":
    main()
