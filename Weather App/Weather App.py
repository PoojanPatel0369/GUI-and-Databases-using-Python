'''
Question:
Build a Weather App to check the Air Quality of Las Vegas.
'''

from tkinter import *
import requests
import json

root = Tk()
root.title('Weather App')
root.iconbitmap('S:\Programming Practice\GitHub\GUI-and-Databases-using-Python\Picture Library\Logo.ico')
root.geometry("400x40")
root.configure(background='green')

#https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=BF28ECF1-11DD-4F3D-A8FA-634E8D659D06

try:
    api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=BF28ECF1-11DD-4F3D-A8FA-634E8D659D06")
    api = json.loads(api_request.content)
    city = api[0]['ReportingArea']
    quality = api[0]['AQI']
    category = api[0]['Category']['Name']

    if category == "Good":
        weather_color = "green"
    elif category == "Moderate":
        weather_color = ""
    elif category == "Unhealthy for Sensitive Groups":
        weather_color = ""
    elif category == "Unhealthy":
        weather_color = ""
    elif category == "Very Unhealthy":
        weather_color = ""
    elif category == "Hazardous":
        weather_color = ""

    myLabel = Label(root, text=city + " Air Quality " + str(quality) + " " + category, font=("Helvetica", 20), background="green")
    myLabel.pack()
    
except Exception as e:
    api = "Error..."



root.mainloop()
