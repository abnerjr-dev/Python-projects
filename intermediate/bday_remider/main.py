import pandas as pd
import datetime as dt
import smtplib
import random as r

today = dt.datetime.now()
this_day = today.day
this_month = today.month

my_email = "abner.teste123@gmail.com"
password = "zrutweguejgzxmxw"

bday_data = pd.read_csv("intermediate/bday_remider/birthdays.csv")

for i in bday_data.iterrows():
    name = i[1]["name"]
    birth_day = i[1]["day"]
    birth_month = i[1]["month"]
    to_email = i[1]["email"]

    if this_day == birth_day and this_month == birth_month:

        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs="barbosa5@msu.edu",
                msg=f"subject:Hoje e aniversario de {name}!!!\n\nNao vai esquecer de mandar parabens pra/o {name}!!!!!!!!!!!!!!!!!!!",
            )
        print("foi")
