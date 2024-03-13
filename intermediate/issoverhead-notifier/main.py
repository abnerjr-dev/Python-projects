import requests
from datetime import datetime
import smtplib
import time

MY_LAT = -23.646560  # Your latitude
MY_LONG = -46.712350  # Your longitude
my_email = "abner.teste123@gmail.com"
password = "zrutweguejgzxmxw"


def is_iss_close():
    global iss_longitude, iss_latitude

    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if (
        MY_LAT - 5 <= iss_latitude <= MY_LAT + 5
        and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5
    ):
        return True
    else:
        return False


def is_dark():

    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
        "tzid": "America/Sao_Paulo",
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise_hr = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset_hr = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    hr_now = time_now.hour

    if hr_now >= sunset_hr or hr_now <= sunrise_hr:
        return True
    else:
        return False


while True:
    if is_iss_close() and is_dark():
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs="barbosa5@msu.edu",
                msg=f"subject:ISS ABOVE!!!\n\nLook up and try and spot it!!!!!!!!!!!!!!!!!!!",
            )

    else:
        print("Conditions not great to spot the ISS")
        print(f"ISS Position:\nLatitude: {iss_latitude}\nLongitude: {iss_longitude}\n")
        print(f"Your Position:\nLatitude: {MY_LAT}\nLongitude: {MY_LONG}")

    time.sleep(60)
