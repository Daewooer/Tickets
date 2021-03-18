age = int(input("Enter age to find out the cost of the movie ticket, or '0' to exit: "))

while age > 0:
    if age < 3:
        print("Your ticket is free.")
        print("Thanks for using our ticket machine")
        break
    elif age < 12:
        print("You're ticket is 10$")
        print("Thanks for using our ticket machine")
        break
    else:
        print("You're ticket is 15$")
        print("Thanks for using our ticket machine")
        break