def get_bmr_male(weight, height, age, imperial=''):
    if imperial:
        weight = float(weight) * 0.45359237
        height = float(height) * 2.54
    bmr_cals_male = (10 * float(weight)) + (6.25 * float(height)) - (5 * int(age)) + 5
    print(f"You are expending {bmr_cals_male} calories just by existing!")


def get_bmr_female(weight, height, age, imperial=''):
    if imperial:
        weight = float(weight) * 0.45359237
        height = float(height) * 2.54
    bmr_cals_female = (10 * weight) + (6.25 * height) - (5 * int(age)) - 161
    print(f"You are expending {bmr_cals_female} calories just by existing!")
    
bmr_questions = True
while bmr_questions:
    print("Find your Basal Metabolic Rate: ")    
    print("(press 'q' to exit) ")
    sex = input("Sex: ").lower()
    
    if sex == "male":
        print("Do you prefer imperial or metric units?")
        imperial = input("'imp' / 'met' ").lower()
        
        weight_male = input("Weight: ")
        if weight_male == 'q':
            break
        height_male = input("Height: ")
        if height_male == 'q':
            break
        age_male = input("Age: ")
        if age_male == 'q':
            break
        if imperial == 'q':
            break
        elif imperial == 'imp':
            get_bmr_male(weight_male, height_male, age_male, imperial)
        elif imperial == 'met':
            get_bmr_male(weight_male, height_male, age_male)
        else:
            print("Sorry, only imperial or metric values work!")
            break
        again = input("Would you like to check another? (y/n) ").lower()
        if again == 'n':
            bmr_questions = False

    elif sex == "female":
        print("Do you prefer imperial or metric units?")
        imperial = input("'imp' / 'met' ").lower()
        
        weight_female = input("Weight: ")
        if weight_female == 'q':
            break
        height_female = input("Height: ")
        if height_female == 'q':
            break
        age_female = input("Age: ")
        if age_female == 'q':
            break
        if imperial == 'q':
            break
        elif imperial == 'imp':
            get_bmr_male(weight_female, height_female, age_female, imperial)
        elif imperial == 'met':
            get_bmr_male(weight_female, height_female, age_female)
        else:
            print("Sorry, only imperial or metric values work!")
            break
        again = input("Would you like to check another? (y/n) ").lower()
        if again == 'n':
            bmr_questions = False

    elif sex == 'q':
        break    
    
    else:
        print("Sorry, this program only works with 'male' and 'female.'")