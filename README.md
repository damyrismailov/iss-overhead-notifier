# ISS Overhead Notifier

Small Python script that checks whether the International Space Station (ISS) is currently above your location at night and sends you an email alert if it is.

## Main features

- Uses `http://api.open-notify.org/iss-now.json` to get the current latitude and longitude of the ISS.
- Uses `https://api.sunrise-sunset.org/json` to get sunrise and sunset times for your coordinates.
- Stores configuration at the top of the file:
  - `MY_EMAIL` – the email address that sends the alert.
  - `APP_PASSWORD` – app password for that email account.
  - `TO_EMAIL` – the email address that receives the alert.
  - `MY_LAT`, `MY_LONG` – your latitude and longitude.
- Converts the ISS coordinates from strings to floats and checks if the ISS is within ±5 degrees of your latitude and longitude.
- Extracts the sunrise and sunset hours from the API response and checks if the current hour is between sunset and sunrise (dark at your location).
- Runs inside an infinite `while True` loop with `time.sleep(60)` to check once per minute.
- When both conditions are true (ISS close to you and it is dark), sends an email with the subject `ISS IS NEAR!` using `smtplib` and `starttls`.

## What I learned

- Making HTTP requests to external APIs using the `requests` library.
- Parsing JSON responses and extracting specific fields.
- Working with dates and times using `datetime.now()` and the `.hour` attribute.
- Comparing geographic coordinates with simple numeric ranges.
- Building a polling loop with `while True` and `time.sleep()` to run checks repeatedly.
- Sending email from Python with `smtplib`, TLS encryption (`starttls`) and login credentials.
- Keeping configuration values (email, password, coordinates) grouped at the top of the script so the main logic stays clean.

## How to run

1. Make sure you have Python 3 installed.
2. Install the `requests` package with `pip install requests`.
3. Open `main.py` and update the configuration section at the top:

   `MY_EMAIL = "your_email@example.com"`  
   `APP_PASSWORD = "your_app_password_here"`  
   `TO_EMAIL = "target_email@example.com"`  
   `MY_LAT = Your_LATITUDE`  
   `MY_LONG = Your_LONGITUDE`

4. If you are not using Gmail, change the SMTP host and port in the line with `smtplib.SMTP("smtp.gmail.com", 587)` to match your own email provider.
5. From the project folder, run `python main.py`.
6. The script will run in a loop, checking every 60 seconds. When the ISS is within ±5 degrees of your position and it is dark at your location, an email with the subject `ISS IS NEAR!` and the message `LOOK UP!!!` will be sent to the address in `TO_EMAIL`. If the conditions are not met, no email is sent and the script continues checking.
