def get_bmr(weight, height, age, sex, imperial=''):
    if imperial:
        weight = float(weight) * 0.45359237
        height = float(height) * 2.54
    bmr_cals = (10 * float(weight)) + (6.25 * float(height)) - (5 * int(age)) + (5 if sex == 'male' else -161)
    print(f"You are expending {bmr_cals} calories just by existing!")


bmr_questions = True
while bmr_questions:
    print("Find your Basal Metabolic Rate: ")    
    print("(press 'q' to exit) ")
    
    sexes = ['male', 'female']
    sex = input("Sex: ").lower()
    if sex == 'q':
        break
    if sex in sexes:
        print("Do you prefer imperial or metric units?")
        imperial = input("'imp' / 'met' ").lower()
        
        weight = input("Weight: ")
        if weight == 'q':
            break
        height = input("Height: ")
        if height == 'q':
            break
        age = input("Age: ")
        if age == 'q':
            break
        if imperial == 'q':
            break
        elif imperial == 'imp':
            get_bmr(weight, height, age, sex, imperial)
        elif imperial == 'met':
            get_bmr(weight, height, age, sex)
        else:
            print("Sorry, only imperial or metric values work!")
            break

        again = input("Would you like to check another? (y/n) ").lower()
        if again == 'n':
            bmr_questions = False
    else:
        print("Sorry, this program only works with 'male' and 'female.'")
        break