import sys
import smtplib
from email.message import EmailMessage
from config import credentials

with open("config/possible-sponsors.txt", "r") as f:
    possible_sponsors = f.read()

with open("data/emailed-sponsors.txt", "r") as f:
    emailed_sponsors = f.read()

possible_sponsors = possible_sponsors.split("\n")
emailed_sponsors = emailed_sponsors.split("\n")
email_list = []

for i in range(len(possible_sponsors)):
    if possible_sponsors[i] not in emailed_sponsors:
        email_list.append(possible_sponsors[i])

print("Sending emails to the following sponsors: ")
print(email_list)

while True:
    confirm = input("Confirm this is ok to continue (Y/n): ")
    if confirm == "Y" or confirm == "y":
        break
    elif confirm == "N" or confirm == "n":
        print("Exiting")
        sys.exit(0)

EMAIL = credentials.EMAIL
PASSWORD = credentials.PASSWORD
i = 0
for i in range(len(email_list)):
    sponsor_name = email_list[i].split(" :: ")[0]
    sponsor_email = email_list[i].split(" :: ")[1]

    msg = EmailMessage()
    msg.set_content("Hello! This is a test email sent via Python.")
    msg['Subject'] = 'Test Subject'
    msg['From'] = EMAIL
    msg['To'] = sponsor_email

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(EMAIL, PASSWORD)
            server.send_message(msg)
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error: {e}")