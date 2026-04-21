import sys

with open("config/possible-sponsors.txt", "r") as f:
    possible_sponsors = f.read()

with open("data/email-sponsors.txt", "r") as f:
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


