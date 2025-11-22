height = input("What is your height in cm? ")
height_int = int(height)
bill = 0

if height_int >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        print("Child ticket is $5.")
        bill = 5
    elif age<=18:
        print("Youth Ticket is $7.")
        bill = 7
    else:
        print("Adult Ticket is $12.")
        bill = 12
    want_photo = input("Do you want a photo taken? Y or N. ")
    if want_photo == "Y":
        # Add $3 to their bill
        bill += 3
    print(f"Your final bill is ${bill}")
else:
    print("Sorry, you have to grow taller before you can ride.")