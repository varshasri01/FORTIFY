import random
import string
def generate_password():
    length=int(input("Enter the password length:"))
    if length<=0:
        print("Password length must be greater than 0!")
    uprcase=input("Include uppercase letters?(y/n):")
    lwrcase=input("Include lowercase letter?(y/n):")
    num=input("Include numbers?(y/n):")
    symbols=input("Include special characters(y/n):")
    chosen_categories=0
    characters=""
    if uprcase.lower()=="y":
        characters+=string.ascii_uppercase
        chosen_categories+=1
    if lwrcase.lower()=="y":
        characters+=string.ascii_lowercase
        chosen_categories+=1
    if num.lower()=="y":
        characters+=string.digits
        chosen_categories+=1
    if symbols.lower()=="y":
        characters+=string.punctuation
        chosen_categories+=1
    if chosen_categories==0:
        print("you must select atleast one character type.")
        return
    if length< chosen_categories:
        print("Password length is too short for the selected character types.")
        return
    password=[]
    if uprcase.lower()=="y":
        password.append(random.choice(string.ascii_uppercase))
    if lwrcase.lower()=="y":
        password.append(random.choice(string.ascii_lowercase))
    if num.lower()=="y":
        password.append(random.choice(string.digits))
    if symbols.lower()=="y":
        password.append(random.choice(string.punctuation))
    while len(password)<length:
        password.append(random.choice(characters))
    random.shuffle(password)
    password="".join(password)
    print("\nGenerated password:",password)