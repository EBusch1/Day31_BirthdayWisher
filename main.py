##################### Extra Hard Starting Project ######################
import datetime as dt
import random
import smtplib
import pandas

MY_EMAIL = ""
MY_PASSWORD = ""

month_day = (dt.datetime.now().month, dt.datetime.now().day)

birthday_data = pandas.read_csv("birthdays.csv")
birthday_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in birthday_data.iterrows()}

if month_day in birthday_dict:
    person_bday = birthday_dict[month_day]
    person_name = person_bday["name"]
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter_template:
        letter = letter_template.read()
        letter = letter.replace("[NAME]", person_name)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=person_bday["email"],
            msg=f"Subject: Happy Birthday, {person_name}!\n\n{letter}")

# 4. Send the letter generated in step 3 to that person's email address.
