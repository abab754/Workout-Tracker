import os
import datetime
import requests

USER = os.environ.get("USER")
PASSWORD = os.environ.get("PASSWORD")
APP_ID = os.environ.get("APP_ID")
APP_KEY = os.environ.get("APP_KEY")

endpt = "https://trackapi.nutritionix.com/v2/natural/exercise"
post_endpt = "https://api.sheety.co/3f4d5e3300cb13f2ad837b1a20c92bb7/workoutTracker/workouts"


today = datetime.datetime.now()
date_string = today.strftime("%d/%m/%Y")
time_string = today.strftime("%X")
headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
}
inpt = input("Tell me about your workout: ")

params = {
    "query": inpt,
    "gender": "MALE",
    "weight_kg": 20,
    "height_cm": 178,
    "age": 19,
}

# post_params = {
#     "workout":{
#         "date": date_string,
#         "time": time_string,
#         "exercise": "test exercise",
#         "duration": "test dur",
#         "calories": "test cals",
#     }
# }

response = requests.post(url=endpt, json=params, headers=headers, auth= (USER, PASSWORD))
exercise_list = response.json()["exercises"]

# print(exercise_list)

for i in exercise_list:
    dur = i["duration_min"]
    cal_burnt = i["nf_calories"]
    exer = i["name"]
    post_params = {
        "workout":{
            "date": date_string,
            "time": time_string,
            "exercise": exer,
            "duration": dur,
            "calories": cal_burnt,
        }
    }
    post_response = requests.post(url=post_endpt, json=post_params, auth=(USER, PASSWORD))

