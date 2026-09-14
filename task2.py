# Assignment 2 - SmartFit Decision-Making Assistant

# Q1: Conditional Statements

age = int(input("Enter your age: "))

if age < 18:
    print("You are eligible for the Teen Fitness Program.")
elif age >= 18 and age <= 40:
    print("You are eligible for the Regular Fitness Program.")
else:
    print("You are eligible for the Senior Wellness Program.")
# Q2: Logical Operators

medical = input("Do you have any medical conditions? (yes/no): ").lower()

if medical == "yes":
    if age >= 40:
        print("Medical clearance required before joining.")
    else:
        print("You can proceed with registration.")
elif medical == "no":
    if age < 40 or medical == "no":
        print("You can proceed with registration.")
else:
    print("Invalid input. Please enter 'yes' or 'no'.")
# Q3: Nested Conditional Statements

membership = input("Choose your membership type (Basic/Premium): ").lower()

if membership == "basic":
    training = input("Do you want personal training? (yes/no): ").lower()

    if training == "yes":
        print("Basic plan with personal training: $45 per month.")
    elif training == "no":
        print("Basic plan: $30 per month.")
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")

elif membership == "premium":
    print("Premium plan: $60 per month.")

else:
    print("Invalid membership type. Please choose Basic or Premium.")


# Nested Conditions with Logical Operators

if membership == "premium" and age < 30:
    print("You qualify for a youth discount! 10% off your plan.")

if membership == "basic" and training == "no":
    print("Consider upgrading to Premium for more benefits!")

if medical == "yes" and membership == "premium":
    print("We recommend a free consultation before starting.")