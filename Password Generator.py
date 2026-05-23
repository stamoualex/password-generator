import random
import string

while True:
    try:
        length = int(input("How long would you like your password to be? "))
        break
    except ValueError:
        print("Please enter a valid number!")

def get_yes_no(prompt):
    while True:
        answer = input(prompt)
        if answer == "y" or answer == "n":
            return answer
        print("Please enter a valid input (y/n)!")
        
numbers = get_yes_no("Include numbers? (y/n): ")
symbols = get_yes_no("Include symbols? (y/n): ")

def create_password(length, numbers, symbols):
    pool = string.ascii_letters
    passWord = ""
    if numbers == "y":
        pool += string.digits
    if symbols == "y":
        pool += string.punctuation
    count = 0
    while count < length:
        passWord += random.choice(pool)
        count += 1
    return passWord

passWord = create_password(length, numbers, symbols)
print(f"Your password is: {passWord}")