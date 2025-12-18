import requests
from datetime import datetime
import smtplib
import time

# --------------------
# CONFIG – CHANGE THESE ONLY
# --------------------
MY_EMAIL = "your_email@example.com"          # your own email address
APP_PASSWORD = "your_app_password_here"      # your email app password
TO_EMAIL = "target_email@example.com"        # where the alert should be sent

MY_LAT = 51.507351                          # your latitude
MY_LONG = -0.127758                          # your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()

sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()
restart = True

while True:
    time.sleep(60)
    if (
        sunset <= time_now.hour <= sunrise
        and MY_LAT - 5 <= iss_latitude <= MY_LAT + 5
        and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5
    ):
        with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=APP_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=TO_EMAIL,
                msg="Subject:ISS IS NEAR!\n\nLOOK UP!!!"
            )
