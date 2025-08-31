import requests
import json
import win32com.client
speaker = win32com.client.Dispatch("SAPI.SpVoice")
city = input("Enter City: ")
url = f"https://api.weatherapi.com/v1/current.json?key=a18d4cfc58cb4210868205743252908&q={city}"
r = requests.get(url)
# print(r.text)
w_dict = json.loads(r.text)
wind_dict = json.loads(r.text)
w = w_dict["current"]["temp_c"]
wi = wind_dict["current"]["wind_kph"]
speaker.speak(f"The current temperature in {city} is {w} degrees celsius and speed of wind is{wi}kilometers per hour.")