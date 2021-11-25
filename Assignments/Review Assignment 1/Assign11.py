height = int(input("Enter height in CM: "))
hip_circumference = int(input("Enter hip circumference in CM: "))
gender = input("Please enter your sex (M/F): ")
age = int(input("Please enter your age: "))

# Calculate BAI
BAI = (hip_circumference / ((height / 100)**1.5)) - 18
print("Your BAI is: {}".format(BAI))
# Printing out appropriate BAI
if gender.upper() == 'F':
    if 20 <= age <= 39:
        if BAI < 21:
            print("Your BAI of {:.1}% is considered UNDERWEIGHT".format(BAI))
        elif 21 <= BAI <= 33:
            print("Your BAI of {:.1}% is considered HEALTHY".format(BAI))
        elif 33 < BAI <= 39:
            print("Your BAI of {:.1}% is considered OVERWEIGHT".format(BAI))
        elif 39 < BAI:
            print("Your BAI of {:.1}% is considered OBESE".format(BAI))

    if 40 <= age <= 59:
        if BAI < 23:
            print("Your BAI of {:.1f}% is considered UNDERWEIGHT".format(BAI))
        elif 23 <= BAI <= 35:
            print("Your BAI of {:.1f}% is considered HEALTHY".format(BAI))
        elif 35 < BAI <= 41:
            print("Your BAI of {:.1f}% is considered OVERWEIGHT".format(BAI))
        elif 41 < BAI:
            print("Your BAI of {:.1f}% is considered OBESE".format(BAI))

    if 60 <= age <= 79:
        if BAI < 25:
            print("Your BAI of {:.1f}% is considered UNDERWEIGHT".format(BAI))
        elif 25 <= BAI <= 38:
            print("Your BAI of {:.1f}% is considered HEALTHY".format(BAI))
        elif 38 < BAI <= 43:
            print("Your BAI of {:.1f}% is considered OVERWEIGHT".format(BAI))
        elif 43 < BAI:
            print("Your BAI of {:.1f}% is considered OBESE".format(BAI))

if gender.upper() == 'M':
    if 20 <= age <= 39:
        if BAI < 21:
            print("Your BAI of {:.1f}% is considered UNDERWEIGHT".format(BAI))
        elif 21 <= BAI <= 33:
            print("Your BAI of {:.1f}% is considered HEALTHY".format(BAI))
        elif 33 < BAI <= 39:
            print("Your BAI of {:.1f}% is considered OVERWEIGHT".format(BAI))
        elif 39 < BAI:
            print("Your BAI of {:.1f}% is considered OBESE".format(BAI))

    if 40 <= age <= 59:
        if BAI < 23:
            print("Your BAI of {:.1f}% is considered UNDERWEIGHT".format(BAI))
        elif 23 <= BAI <= 35:
            print("Your BAI of {:.1f}% is considered HEALTHY".format(BAI))
        elif 35 < BAI <= 41:
            print("Your BAI of {:.1f}% is considered OVERWEIGHT".format(BAI))
        elif 41 < BAI:
            print("Your BAI of {:.1f}% is considered OBESE".format(BAI))

    if 60 <= age <= 79:
        if BAI < 25:
            print("Your BAI of {:.1f}% is considered UNDERWEIGHT".format(BAI))
        elif 25 <= BAI <= 38:
            print("Your BAI of {:.1f}% is considered HEALTHY".format(BAI))
        elif 38 < BAI <= 43:
            print("Your BAI of {:.1f}% is considered OVERWEIGHT".format(BAI))
        elif 43 < BAI:
            print("Your BAI of {:.1f}% is considered OBESE".format(BAI))
