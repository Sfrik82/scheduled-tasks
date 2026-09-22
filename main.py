import smtplib
import os
import pandas
import datetime as dt
from random import randint
MY_EMAIL = os.environ.get("MY_EMAIL") #"neroiddf@gmail.com"
PASSWORD = os.environ.get("MY_PASSWORD")#"aqdvejsgqwxawuae"

date = dt.datetime.now()
today =  (date.month, date.day)

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today in birthdays_dict:
    birthdays_person = birthdays_dict[today]
    file_path = f"letter_templates/letter_{randint(1,3)}.txt"
    with open(file_path) as f:
        contents = f.read()
        message = contents.replace("[NAME]", f"{birthdays_person["name"]}")
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
     connection.starttls()
     connection.login(user=MY_EMAIL, password=PASSWORD)
     connection.sendmail(from_addr=MY_EMAIL,
                         to_addrs=f"{birthdays_person['email']}",
                         msg=f"Subject:Hello\n\n{message}"
     )