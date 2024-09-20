import smtplib
import requests
from pprint import pprint
from datetime import datetime
import time

from dotenv import load_dotenv
import os

load_dotenv()


my_email = os.getenv("my_email")
password = os.getenv("password")


MY_LAT = 12.971599
MY_LONG = 77.594566

sunrise_sunset_api = "https://api.sunrise-sunset.org/json"
iss_current_position_api = "http://api.open-notify.org/iss-now.json"


def get_sunrise_sunset_hours():

    params = {"lat": MY_LAT,
              "lng": MY_LONG,
              "date": datetime.now().date(),  # ""2024-09-20"",
              "formatted": 0
              }

    response = requests.get(url=sunrise_sunset_api, params=params)
    response.raise_for_status()
    data = response.json().get('results')

    sunrise = int(data.get('sunrise').split("T")[1].split(":")[0]) + 5
    sunset = int(data.get('sunset').split("T")[1].split(":")[0]) + 5

    print("sun rise and set?")
    print(sunrise, sunset)
    return sunrise, sunset


def iss_current_lat_long():
    response = requests.get(url=iss_current_position_api)
    response.raise_for_status()
    data = response.json().get('iss_position')
    return float(data.get('latitude')), float(data.get('longitude'))


def send_email(subject, message, to_email, user_email, user_password, email_provider="smtp.gmail.com"):
    """email_provider: Gmail (smtp.gmail.com), Yahoo (smtp.mail.yahoo.com), 
    Hotmail (smtp.live.com), Outlook (smtp-mail.outlook.com)"""
    with smtplib.SMTP(email_provider) as connection:  # gmail smtp server
        connection.starttls()  # for encryption
        try:
            connection.login(user=user_email, password=user_password)
            connection.sendmail(from_addr=user_email,
                                to_addrs=user_email,
                                msg=f"Subject:{subject}\n\n{message}")
            print(f"Message Sent to {to_email}!")
        except Exception:
            print("Error! Message not sent")


def send_iss_overhead_alert():
    send_email(subject="ISS Overhead!!!",
               message=f"Quick! Go out and look up to see the ISS",
               to_email="nithishkr136@yahoo.com",
               user_email=my_email,
               user_password=password)


def iss_overhead_check():
    iss_lat, iss_long = iss_current_lat_long()
    print("Iss lat long")
    print(iss_lat, iss_long)
    if (MY_LAT-5 <= iss_lat <= MY_LAT+5) and (MY_LONG-5 <= iss_long <= MY_LONG+5):
        return True
    else:
        return False


def is_it_night():
    sunrise_hour, sunset_hour = get_sunrise_sunset_hours()
    now_hour = datetime.now().hour
    if now_hour >= sunset_hour or now_hour <= sunrise_hour:
        return True
    else:
        return False


while True:
    if iss_overhead_check() and is_it_night():
        send_iss_overhead_alert()
    time.sleep(60)
