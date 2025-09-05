import requests
import json
import win32com.client
speaker = win32com.client.Dispatch("SAPI.SpVoice")
city = input("Enter City: ")
url = f"YOU_AI_KEY{city}"
r = requests.get(url)
# print(r.text)
w_dict = json.loads(r.text)
wind_dict = json.loads(r.text)
w = w_dict["current"]["temp_c"]
wi = wind_dict["current"]["wind_kph"]
speaker.speak(f"The current temperature in {city} is {w} degrees celsius and speed of wind is{wi}kilometers per hour.")
