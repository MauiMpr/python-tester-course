
action = input("Do you like action? (yes/no): ") == "yes"
comedy = input("Do you like comedy? (yes/no): ") == "yes"
sci_fi = input("Do you like sci_fi? (yes/no): ") == "yes"

if action and comedy and not sci_fi:
    genre = "action-comedy"
elif action and sci_fi and not comedy:
    genre = "action-sci_fi"
elif comedy and sci_fi and not action:
    genre = "comedy-sci_fi"
elif action:
    genre = "action"
elif comedy:
    genre = "comedy"
elif sci_fi:
    genre = "sci_fi"
else:
    genre = "Unknown"

if genre == "action-comedy":
        print("Recommended Movies: Rush Hour, Bad Boys, The Nice Guy")
elif genre == "action-sci_fi":
        print("Recommened Movies: The Martian, Interstellar")
elif genre == "comedy-sci_fi":
        print("Recommended Movies: Guardians Of The Galaxy")
elif genre == "action":
        print("Recommened Movies: Die Hard, Ride Along")
elif genre == "comedy":
        print("Recommened Movies: Central Intelligence, Dealpool")
elif genre == "sci_fi":
        print("Recommened Movies: Aliens, Avengers")
else:
        print("Sorry, we dont know what you like")