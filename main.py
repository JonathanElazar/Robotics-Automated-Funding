with open("config/possible-sponsors.txt", "r") as f:
    possible_sponsors = f.read()

with open("data/email-sponsors.txt", "r") as f:
    emailed_sponsors = f.read()

possible_sponsors = possible_sponsors.split("\n")
emailed_sponsors = emailed_sponsors.split("\n")

for i in range(len(possible_sponsors)):
    
