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
