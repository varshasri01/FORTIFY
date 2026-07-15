import modules.password_checker_v2 as strength_checker
import modules.password_generator_v2 as generator
import modules.password_leak_checker as leak_checker
print("="*50)
print("     FORTIFY v1.0")
print("    Cybersecurity Toolkit")
print("="*50)

print("\nSelect an option:")

print("1.Password Strength Checker")
print("2.Password Generator")
print("3. Password Leak Checker")
print("4.Exit")
choice=input("\nEnter your choice:")
if choice=="1":
    strength_checker.check_password()
elif choice=="2":
    generator.generate_password()
elif choice=="3":
    password=input("Enter a password to check:")
    count=leak_checker.check_password(password)
    if count:
        print(f"\nThis password has appeared {count} times in data branches!")
    else:
        print("\nGood news! This password was NOT found in known branches.")
elif choice=="4":
    print("Thank you for using Fortify!")
else:
    print("\nInvalid choice! please select the valid options:")
    