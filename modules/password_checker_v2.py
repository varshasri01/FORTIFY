def check_password():
    print("=== Password Strength Checker ===")
    password=input("Enter your Password:")
    print("Password Received:",password)
    score=0
    if len(password)>=8:
        print("Password length is good.")
        score+=1
    else:
        print("Password is too short.")
        print("Suggestion: Make your password atleast 8 characters long.")
    has_upper= False
    has_lower= False
    has_digit= False
    special_characters="@#$%^&*!?"
    has_splchr= False
    for letter in password:
        if letter.isupper():
            has_upper= True
        if letter.islower():
            has_lower= True
        if letter.isdigit():
            has_digit= True
        if letter in special_characters:
            has_splchr= True
    if has_upper:
        print("Uppercase letter found.")
        score+=1
    else:
        print("No uppercase letter is found.")
        print("Suggestion: Add atleast one uppercase letter.")
    if has_lower:
        print("Lowercase letter found.")
        score+=1
    else:
        print("No lowercase letter is found.")
        print("Suggestion: Add atleast one lowercase letter.")
    if has_digit:
        print("Digits are found.")
        score+=1
    else:
        print("Digits not found.")
        print("Suggestion: Add atleast one number.")
    if has_splchr:
        print("Special characters found")
        score+=1
    else:
        print("No special characters found.")
        print("Suggestion: Add atleast one special character.")
    print("="*40)
    print("FORTIFY SECURITY REPORT")
    print("="*40)
    print("Password Score:",score, "/5")
    if score==5:
        print("Excellent!! your password meets all security requirements.")
    elif score==4:
        print("Strong Password! Consider minor imporvement is needed.")
    elif score==3:
        print("It's  a medium strength password.")
    else:
        print("Oops, it's weak password.") 
    if not(has_upper and has_lower and has_digit and has_splchr and len(password)>=8):
        print("Recommendations:")
    if not has_upper:
        print("` Add atleast one uppercase letter.")
    if not has_lower:
        print("` Add atleast one lowercase letter.")
    if not has_digit:
        print("` Add atleast one digit.")
    if len(password)<8:
        print("` use atleast 8 characters.")
    print("="*40)