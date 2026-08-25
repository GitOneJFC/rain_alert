# To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.
import random
import pandas as pd
import datetime as dt
import smtplib
import os

#GIT secrets:
MY_EMAIL = os.environ.get("MY_EMAIL1")
MY_PASSWORD = os.environ.get("MY_PASSWORD1")

#TODO 1: Updating birthdays.csv
#TODO 2: Check if today matches a birthday in the birthdays.csv
# Read data from csv
today = dt.datetime.now()
day = today.day
month = today.month
year = today.year

list = pd.read_csv('birthdays.csv')
dates_list = [(list.month[item], list.day[item]) for item in range(list.index.size)]

list.insert(5, 'birthdate',dates_list,True)
# ------------------------------------------------------------------
rec_index = list.index[list['birthdate']==(month,day)].tolist()

# ---------------------------------------------------------------------
rec_df = list[list['birthdate'] == (month, day)]

# -----------------------------------------------------------------------

#TODO 3 - Letter Selection
folder = './letter_templates/'
birthday_msg = random.choice(['letter_1.txt', 'letter_2.txt', 'letter_3.txt'])

for i in rec_index:
    with open(folder + birthday_msg,'r') as msg:
        text = msg.read()
        text = text.replace('[NAME]', list.name[i])
    print(text)
    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL1,MY_PASSWORD1)
        connection.sendmail(
            from_addr = MY_EMAIL,
            to_addrs = list.email[i],
            msg = f"Subject: Happy Birthday!\n\n {text}"
        )
    print("Message Sent")
