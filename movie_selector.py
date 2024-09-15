action = input("Do you like action? (yes/no): ")
comedy = input("Do you like comedy? (yes/no): ") 
sci_fi = input("Do you like sci_fi? (yes/no): ") 

if action and comedy and not sci_fi:
    genre = "Action-Comedy"
elif action and sci_fi and not comedy:
    genre = "Action-Scy_Fi"
elif comedy and sci_fi and not action:
    genre = "Comedy-Sci_fi"
elif action:
    genre = "Action"
elif comedy:
    genre = "Comedy"
elif sci_fi:
    genre = "Sci_Fi"
else:
    genre = "Unknown"

    if genre == "Action-Comedy":
        print("Recommended Movies: Rush Hour, Bad Boys, The Nice Guy")
    elif genre == "Action-Sci_Fi":
        print("Recommened Movies: The Martian, Interstellar")
    elif genre == "Comedy-Sci_Fi":
        print("Recommended Movies: Guardians Of The Galaxy")
    elif genre == "Action":
        print("Recommened Movies: Die Hard, Ride Along")
    elif genre == "Comedy":
        print("Recommened Movies: Central Intelligence, Dealpool")
    elif genre == "Sci_Fi":
        print("Recommened Movies: Aliens, Avengers")
    else:
        print("Sorry, we dont know what you like")