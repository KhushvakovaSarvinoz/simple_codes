import re
phone_num= input("Please, enter your phone number:\n")
eg='^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$'
while True:
    if re.match (eg,phone_num):
        print("You phone number accepted")  
        break
    else:
        print("Try again")
        break

