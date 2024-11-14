import yr_weather
import datetime
import uuid

def main():
    get_forcastData()

def get_forcastData() -> dict:
    headers = {"User-Agent": "matiss.zigalvis@gmail.com"}
    my_client = yr_weather.Locationforecast(headers=headers)
        
    forcast = my_client.get_forecast(56.94, 24.10)
    timeseries_list = forcast._timeseries

    forcastDic = {}
    currnetDay = None
    dayAfterTomorrow = None

    for item in timeseries_list:
        
        unique_id = str(uuid.uuid4())

        for key, value in item.items():
                
            if key == "time":              
                datetimeObj = datetime.datetime.strptime(value, "%Y-%m-%dT%H:%M:%SZ")
                datetimeObj = datetimeObj + datetime.timedelta(hours=2)
                currnetDay = datetimeObj.date()

            if dayAfterTomorrow is None:
                dayAfterTomorrow = currnetDay + datetime.timedelta(days=1)
                                                
            if currnetDay <= dayAfterTomorrow and key == "data":
                    for data_key, data_item in value.items():
                        if data_key == "instant":
                            for instant_key, instant_item in data_item.items():
                                if instant_key == "details":
                                    for details_key, details_item in instant_item.items():
                                        if details_key == "air_temperature":
                                            forcastDic[unique_id] = {"time ": datetimeObj, details_key : details_item}

    return forcastDic
            


    if __name__ == "__main__":
        main()