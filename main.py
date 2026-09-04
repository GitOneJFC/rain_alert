import requests
import os
from twilio.rest import Client
import smtplib

import smtplib
# import json

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
API_KEY = os.environ.get("API_KEY")

TWILIO_SMS = ""
TWILIO_API_KEY = ""

MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")
RECIPIENT = os.environ.get("RECIPIENT_EMAIL")


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = ""
auth_token = ""

MY_LAT = os.environ.get('MY_LAT')
MY_LONG = os.environ.get("MY_LONG")

print(f"{MY_EMAIL}, {API_KEY}, {MY_LAT}")

RAIN_LAT = 13
RAIN_LONG = -110

URL_CURRENT = "https://api.openweathermap.org/data/2.5/weather"

URL_5DAY = "https://api.openweathermap.org/data/2.5/forecast"

parameters = {
    'lat': MY_LAT,
    'lon': MY_LONG,
    'cnt': 4,
    'appid': API_KEY,
}
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

response = requests.get(URL_5DAY,params = parameters)
response.raise_for_status()
# print(response.status_code)
data = response.json()
print(f"{data}\n")

print(data['list'][0]['weather'][0]['id'])

rain12 = False

for hour in data['list']:
    # print(hour['weather'][0]['id'])
    condition_code = hour['weather'][0]['id']
    if int(condition_code) < 700:
        rain12 = True
# print(condition_list)
####################################NOTIFY BY TWILIO
# if rain12:
#     client = Client(account_sid, auth_token)
#     message = client.messages.create(
#         to="whatsapp:",
#         from_="whatsapp:",
#         body="test",
#     )
#     print(message.status)
# # "sms_internal_alerts"
# # "It's going to rain today. Remember to bring an Umbrella!☂️"

# #####################NOTIFY BY EMAIL###########################
if rain12:
    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=RECIPIENT,
            msg = f"Subject: Weather Alert!\n\n Look Up! t's going to rain today. Remember to bring an Umbrella!"
        )

################################NOTIFY BY WHATSAPP AND TWILIO#############################


