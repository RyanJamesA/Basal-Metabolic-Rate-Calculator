def get_bmr_male(weight, height, age):
    bmr_cals_male = (10 * float(weight)) + (6.25 * float(height)) - (5 * float(age)) + 5
    print("You are expending " + str(bmr_cals_male) + " calories just by existing!")

def get_bmr_female(weight, height, age):
    bmr_cals_female = (10 * float(weight)) + (6.25 * float(height)) - (5 * float(age)) - 161
    print("You are expending " + str(bmr_cals_female) + " calories just by existing!")
    

bmr_questions = True

while bmr_questions:
    print("For your basal metabolic rate, please enter your sex (male/female): ")
    print("(press 'q' to exit) ")
    sex = input("Sex: ").lower()
    if sex == "male":
        print("Now please enter your weight, height, and age: ")
        print("For weight, please choose your preferred unit: ")
        print("(press 'q' to exit) ")
        lbs_or_kgs = input("Enter 'kg' or 'lbs' ").lower()
        if lbs_or_kgs == 'kg':
            total_weight_male = float(input("Weight: "))
        if lbs_or_kgs == 'lbs':
            weight_male = float(input("Weight: "))
            total_weight_male = weight_male * 0.45359237
        if lbs_or_kgs == 'q':
            break
        
        
        print("For height, please choose your preferred unit: ")
        print("(press 'q' to exit)")
        in_or_cm = input("Enter 'in' or 'cm' ").lower()
        if in_or_cm == 'cm':
            total_height_male = float(input("Height: "))
        if in_or_cm == 'in':
            height_male = float(input("Height: "))
            total_height_male = height_male * 2.54
        if in_or_cm == 'q':
            break
    

        print("For age, please enter your age in years (eg: 18) ")
        print("(press 'q' to exit) ")
        age_male = int(input("Age: "))
        if age_male == 'q':
            break
        
            
        get_bmr_male(float(total_weight_male), float(total_height_male), age_male)
    

    

    elif sex == "female":
        print("Now please enter your weight, height, and age: ")
        print("For weight, please choose your preferred unit: ")
        print("(press 'q' to exit)")
        lbs_or_kgs = input("Enter 'kg' or 'lbs' ").lower()
        if lbs_or_kgs == 'kg':
            total_weight_female = float(input("Weight: "))
        if lbs_or_kgs == 'lbs':
            weight_female = float(input("Weight: "))
            total_weight_female = weight_female * 0.45359237
        if lbs_or_kgs == 'q':
            break

        print("For height, please choose your preferred unit: ")
        print("(press 'q' to exit) ")
        in_or_cm = input("Enter 'in' or 'cm' ").lower()
        if in_or_cm == 'in':
            height_female = float(input("Height: "))
            total_height_female = height_female * 2.54
        if in_or_cm == 'cm':
            total_height_female = float(input("Height: "))
        if in_or_cm == 'q':
            break

        print("For age, please enter your age in years (eg: 18) ")
        print("(press 'q' to exit) ")
        age_female = int(input("Age: "))
        if age_female == 'q':
            break

        get_bmr_female(float(total_weight_female), float(total_height_female), age_female)

        

    elif sex == 'q':
        break

    again = input("Would you like to check another? ").lower()
    if again == 'no':
        bmr_questions = False


