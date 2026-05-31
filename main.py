import random
from datetime import datetime

study_tips = [
    "Study for 25 minutes and take a 5-minute break.",
    "Make short notes while studying.",
    "Practice previous question papers.",
    "Revise regularly to improve memory."
]

quotes = [
    "Success is the sum of small efforts repeated daily.",
    "Believe in yourself and all that you are.",
    "Dream big and work hard.",
    "Every day is a new opportunity to learn."
]

name = input("Enter your name: ")

print(f"\nHello, {name}! Welcome to Smart Student Assistant.\n")

while True:
    print("\n----- MENU -----")
    print("1. Generate Study Tip")
    print("2. Generate Motivation Quote")
    print("3. Display Current Date & Time")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        tip = random.choice(study_tips)
        print("Study Tip:", tip)

        with open("output.txt", "a") as file:
            file.write("Study Tip: " + tip + "\n")

    elif choice == "2":
        quote = random.choice(quotes)
        print("Motivation Quote:", quote)

        with open("output.txt", "a") as file:
            file.write("Motivation Quote: " + quote + "\n")

    elif choice == "3":
        current_time = datetime.now()
        print("Current Date & Time:", current_time)

        with open("output.txt", "a") as file:
            file.write("Date & Time: " + str(current_time) + "\n")

    elif choice == "4":
        print("Thank you!")
        break

    else:
        print("Invalid Choice")
