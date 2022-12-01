import string
import random

characters = list(string.ascii_letters + string.digits +"!@#$%^&*()")

def generate_password():
    password_length = int(input("how long would you like your password?"))

    random.shuffle(characters)

    password = []

    for x in range(password_length):
        password.append(random.choice(characters))

    random.shuffle(password)


    password = "".join(password)

    print(password)


option = input("do you want to generate a password? (yes/n): ")

if option == "yes":
    generate_password()
elif option == "no":
    print("program ended")
    quit()
else:
    print("invalid input,please input yes or no")
    quit()
