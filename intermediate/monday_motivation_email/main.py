import datetime as dt
import smtplib
import random as r

now = dt.datetime.now()
day_of_week = now.weekday()

my_email = "abner.teste123@gmail.com"
password = "zrutweguejgzxmxw"

if day_of_week == 0:
    quotes = open("intermediate/monday_motivation_email/quotes.txt").readlines()
    quote = r.choice(quotes)
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="abner.teste@yahoo.com",
            msg=f"subject:You got this!\n\n{quote}",
        )
