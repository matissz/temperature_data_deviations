# import time
# current_time = time.localtime()
# print(current_time)

import datetime

forcastDic = {
    "datetime" : "",
    "air_temperature" : ""
}

forcastDic["datetime"] = "2024-11-11 04:00:00"
forcastDic["air_temperature"] = "2.3"



value = "2024-11-11T04:00:00Z"

datetimeObj = datetime.datetime.strptime(value, "%Y-%m-%dT%H:%M:%SZ")

currnetDay = datetimeObj.date()
dayAfterTomorrow = None




print(f"currnetDay {currnetDay} is equals to dayAfterTomorrow {dayAfterTomorrow} : {currnetDay == dayAfterTomorrow}")

