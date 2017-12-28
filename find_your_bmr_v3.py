import sys

def main():
    """Calls the other functions and then calls my_calculations()"""
    print("\n\tWelcome to the BMR calculator!")
    print("\tPress 'q' at any time to stop!")
    active = True
    while active:
        units = get_unit()
        sex = get_sex()
        age = get_age()
        height = get_height()
        weight = get_weight()
        my_calculations(units, sex, age, height, weight)

def get_unit():
    """Lets the user set his unit preference"""
    print("\nDo you prefer Imperial or Metric units?")
    imp_or_met_input = input("imp/met: ")
    while True:
        if imp_or_met_input == 'imp' or imp_or_met_input == 'met':
            return imp_or_met_input
        if imp_or_met_input == 'q':
            sys.exit()
        else:
            print("Sorry, only 'met' and 'imp' works.")
            get_unit()

def get_sex():
    """Lets the user set his sex"""
    print("\nWhat is your sex?")
    get_sex_input = input("male/female: ")
    while True:
        if get_sex_input == 'male' or get_sex_input == 'female':
            return get_sex
        if get_sex_input == 'q':
            sys.exit()
        else:
            print("Sorry, only 'male' and 'female' inputs work!")
            get_sex()

def get_age():
    """Lets the user set his age"""
    try:
        print("\nHow old are you? ")
        age_input = input("ex 18: ")
        if age_input == 'q':
            sys.exit()
        else:
            age_input = int(age_input)
            return age_input
    except ValueError:
        print("Sorry, numbers only please!")
        get_age()

def get_height():
    """Lets the user set his height"""
    try:
        print("\nHow tall are you?")
        height_input = input("ex 73: ")
        if height_input == 'q':
            sys.exit()
        else:
            return float(height_input)
    except ValueError:
        print("Sorry, numbers only please!")
        get_height()

def get_weight():
    """Lets the user set his weight"""
    try:
        print("\nHow much do you weigh?")
        weight_input = input("ex 202/70: ")
        if weight_input == 'q':
            sys.exit()
        else:
            return float(weight_input)
    except ValueError:
        print("Sorry, numbers only please!")
        get_height()

def my_calculations(units, sex, age, height, weight):
    """Combines the measurements gathered from main() and does calculations"""
    if units == 'imp':
        user_height = height * 2.54
        user_weight = weight * 0.45359237
        bmr_cals = (user_weight * 10) + (user_height * 6.25) - (5 * age) 
        + (5 if sex == 'male' else -161)
        print(f"You are expending {bmr_cals} calories just by existing!")
    if units == 'met':
        bmr_cals = (weight * 10) + (height * 6.25) - (5 * age) 
        + (5 if sex == 'male' else -161)
        print(f"You are expending {bmr_cals} calories just by existing!")
    start_again()

def start_again():
    while True:
        print("\nWould you like to do another one?")
        user_response = input("y/n ")
        if user_response == 'y':
            main()
        if user_response == 'n' or user_response == 'q':
            sys.exit()
        else:
            print("Sorry, the only valid responses are y/n/q")

main()
