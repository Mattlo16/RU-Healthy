def main():
    print("Welcome to our RU-Healthy!")
    print("By Matthew Loaces and Sean Dong")
    print("*********************************")
    print("")

    print("⠀⠀⢀⣤⣾⣿⣿⣿⣿⣿⣶⣤⡀⢀⣤⣶⣿⣿⣿⣿⣿⣷⣤⡀⠀⠀")
    print("⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀")
    print("⢠⣿⣿⣿⣿  _____  __    _  ⣿⣿⣿⣿⣿⣿⡄")
    print("⢸⣿⣿⣿⣿ |  __ \|  |  | | ⣿⣿⣿⣿⣿⣿⡇")
    print("⠀⣿⣿⣿⣿ | |__) |  |  | | ⣿⣿⣿⣿⣿⣿⠀")
    print("⠀⠘⣿⣿⣿ |  _  /|  |  | | ⣿⣿⣿⣿⣿⠃⠀")
    print("⠀⠀⠈⢿⣿ | | \ \|  |__| | ⣿⣿⣿⡿⠁⠀⠀")
    print("⠀⠀⠀⠀⠙⢿|_|  \_\_\_____/ ⣿⡿⠋⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀ ⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠀ ⠀⠙⢿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠉⠻⣿⣿⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ⠀⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("")
    print("")



    firstName = input("Please enter your first name: ")
    lastName = input("Please enter your last name: ")
    age = int(input("Please enter your age: "))
    x = True
    while x:
        gender = input("Please enter your gender (male/female): ")
        if gender == 'male' or gender == 'female':
            x = False
        else:
            print("Invalid input, please enter (male/female).")
    while age < 0:
        print("You have entered an invalid input")
        print("Please try again.")
        age = int(input("Please enter your age: "))

    continueCode = True
    while continueCode == True:

        print("")
        print("Here is a list of available functions:")
        print("1. RU Sleep 😴")
        print("2. RU BMI 🧮")
        print("3. RU Calorie 🍕")
        print("4. RU Active 🏃‍")
        print("5. RU Nutritious 🍽")
        print("")
        while True:
            try:
                function_num = int(input("Please enter what function you would like to do: "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid number from 1 - 6.")
        if function_num == 1:
            RU_Sleep(age, firstName)
        elif function_num == 2:
            RU_BMI(firstName)
        elif function_num == 3:
            RU_Calorie(firstName, age, gender)
        elif function_num == 4:
            RU_Active(firstName, age)
        elif function_num == 5:
            RU_Nutritious(firstName, age, gender)

        x = 0
        while x == 0:
            conditionTester = input("Would you like to continue? (Press y/n): ")
            if conditionTester == 'y':
                x = 1
                continueCode = True
            elif conditionTester == 'n':
                x = 1
                continueCode = False
            else:
                print("You have entered invalid input, please try again.")


#Function #1
def RU_Sleep(age, firstName):
    print("")
    print("")
    print("Welcome", firstName, "to RU-Sleep!")
    print("")
    if age <= 2 and age > 0:
        print("Since you are", age, "years old, it is recommended that you should sleep for at least 12 to 16 hours everyday!")
    elif age <= 5 and age > 2:
        print("Since you are", age, "years old, it is recommended that you should sleep for at least 11 to 14 hours everyday!")
    elif age <= 12 and age > 5:
        print("Since you are", age, "years old, it is recommended that you should sleep for at least 10 to 13 hours everyday!")
    elif age <= 18 and age > 12:
        print("Since you are", age, "years old, it is recommended that you should sleep for at least 9 to 12 hours everyday!")
    elif age <= 60 and age > 18:
        print("Since you are", age, "years old, it is recommended that you should sleep for at least 7 or more hours everyday!")
    elif age > 60:
        print("Since you are", age, "years old, it is recommended that you should sleep for at least 7 hours everyday!")
    print("")
    print("Good sleep improves your brain performance, mood, and health.")
    print("Not getting enough quality sleep regularly may put yourself at risk in getting diseases and disorders such as:")
    print("     * Heart Disease")
    print("     * Kidney Disease")
    print("     * High Blood Pressure")
    print("     * Diabetes")
    print("     * Stroke")
    print("     * Obesity")
    print("     * Depression")
    print("And many more.")
    print("To prevent this, please sleep for the recommended hours mentioned above! 😀")
    print("") #

#Function #2
def RU_BMI(firstName):
    print("")
    print("")
    print("Welcome ", firstName," to the BMI-checker!", sep='')
    print("")
    print("This function allows you to check your BMI and learn about what a BMI even is!")
    print("")
    print("A BMI, or Body Mass Index, is a measure of body fat, based on one's height and weight.")
    print("We will use your weight and height to calculate if the amount of body fat you have is a healthy or unhealthy amount.")
    print("")
    print("To get started, we're first going to need some info from you.")
    print("")
    weight = int(input("Please enter your weight in pounds(lb): "))
    HeightFeet = int(input("Please enter your height in feet: "))
    HeightInches = int(input("Please enter your height in inches: "))
    Height_both_inches = HeightInches + (HeightFeet * 12)
    bmi = (weight/((Height_both_inches)**2) * 703)
    bmi = round(bmi, 2)
    print("Thank you")
    print("")
    print("")



    print("Your BMI is", bmi)

    if 0 < bmi < 18.5:
        print("With a BMI of ", bmi, ", you are considered underweight.", sep='')
        print("People that are underweight are at risk of certain health conditions such as: ")
        print("     * Malnutrition")
        print("     * Osteoporosis")
        print("     * Decreased muscle strength")
        print("     * Hypothermia")
        print("     * Lowered immunity")
        print("And many more.")
        print("If you are underweight, it is very important that you eat a variety of foods that will give you the nutrition you need.")
        print("The aim is to gain weight gradually by eating healthy foods.")
        print("Even if you are underweight, try to avoid foods with a lot of added sugar, fat and salt, like cakes, takeaway foods and sugary drinks.")
        print("Don't worry though, if you follow these tips you should eventually lose weight and be healthy! 😀")
        print("")
    elif 18.5 <= bmi <= 24.9:
        print("With a BMI of ", bmi, ", you are considered normal weight.", sep='')
        print("Being normal weight is incredibly good because it means that you are not at risk of any health conditions that overweight people have to deal with.")
        print("Continue eating healthy foods and having a balanced diet, because you are HEALTHY! 😀")
        print("")
    elif 25 <= bmi <= 29.9:
        print("With a BMI of ", bmi, ", you are considered overweight.", sep='')
        print("People who are overweight are at a slight risk for many diseases and health conditions such as:")
        print("     * High Blood Pressure")
        print("     * High Cholesterol")
        print("     * Stroke")
        print("     * Sleep apnea")
        print("     * Type 2 diabetes")
        print("And many more.")
        print("While there are many different ways of reducing your bmi and weight, the number one way to do so is to choose healthier foods.")
        print("These include: Whole grains, fruits, vegetables, healthy fats, and protein sources.")
        print("Reduce and limit the amount of unhealthy sugary foods you eat.")
        print("Don't worry though, if you follow these tips, you should eventually lose weight and be healthy! 😀")
        print("")
    elif bmi >= 30:
        print("With a BMI of ", bmi, ", you are considered obese.", sep='')
        print("People who have obesity are at an increased risk for many diseases and health conditions such as:")
        print("     * High Blood Pressure")
        print("     * High Cholesterol")
        print("     * Stroke")
        print("     * Sleep apnea")
        print("     * Type 2 diabetes")
        print("And many more.")
        print("While there are many different ways of reducing obesity, the number one way to do so is to choose healthier foods.")
        print("These include: Whole grains, fruits, vegetables, healthy fats, and protein sources.")
        print("Reduce and limit the amount of unhealthy sugary foods you eat.")
        print("Don't worry though, if you follow these tips, you should eventually stop being obese and be healthy! 😀")
        print("")

#Function #3
def RU_Calorie(firstName, age, gender):
    print("")
    print("")
    print("Welcome", firstName, "to the calorie calculator!")
    print("Here we track how many calories you need to alter your current body weight.")
    print("")
    print("Choose between lose/gain/maintain your current body weight!")
    print("")

    while True:
        goal = input("What is your goal? (lose/gain/maintain): ")
        if goal in ["lose", "gain", "maintain"]:
            break
        else:
            print("Invalid goal input. Please specify 'lose', 'gain', or 'maintain'.")

    while True:
        try:
            weight_pounds = float(input("Please enter your weight in pounds: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number for weight.")

    while True:
        try:
            height_feet = int(input("Please enter your height in feet: "))
            height_inches = int(input("Please enter your height in inches: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number for height.")

    while True:
        activity_level = input("Please enter your activity level (sedentary/lightly active/moderately active/very active/extra active): ")
        if activity_level in ["sedentary", "lightly active", "moderately active", "very active", "extra active"]:
            break
        else:
            print("Invalid activity level input. Please choose from:",
                  ", ".join(["sedentary", "lightly active", "moderately active", "very active", "extra active"]))

    height_inches = (height_feet*12) + height_inches

    height_feet = height_inches/12

    weight_kg = weight_pounds * 0.453592
    height_cm = height_feet * 30.48

    if gender == "male":
        bmr_constant = 5
    elif gender == "female":
        bmr_constant = -161

    bmr = 10 * weight_kg + 6.25 * height_cm - 5 * age + bmr_constant

    activity_factors = {
        "sedentary": 1.2,
        "lightly active": 1.375,
        "moderately active": 1.55,
        "very active": 1.725,
        "extra active": 1.9
    }
    if activity_level not in activity_factors:
        print("Invalid activity level input. Please choose from:", ", ".join(activity_factors.keys()))
        return

    # Calculate daily calorie needs
    calorie_calculation = round(bmr * activity_factors[activity_level])

    print("")

    if goal == "lose":
        calorie_calculation -= 500  # Subtract 500 calories/day for weight loss
        print("To lose weight, you should consume approximately", calorie_calculation, "calories/day. :D")
        print("")
    elif goal == "gain":
        calorie_calculation += 500  # Add 500 calories/day for weight gain
        print("To gain weight, you should consume approximately", calorie_calculation, "calories/day. :D")
    elif goal == "maintain":
        print("To maintain your current weight, you should consume approximately", calorie_calculation, "calories/day. :D")
    else:
        print("Invalid goal input. Please specify 'lose', 'gain', or 'maintain'.")

    print("")
    return calorie_calculation

#Function #4
def RU_Active(firstName, age):
    print("")
    print("")
    print("Welcome to RU Active!")
    print("This function allows you to see if you are active enough and learn about how you can get started with physical activity exercises!")
    print("")
    print("")
    if 5 <= age < 18:
        print("Since you are ", age, " years old, you will need a minimum of 60 minutes of moderate to vigoous physical activity a day.", sep='')
        print("At least 3 days a week should include vigorous aerobic activity and activities that build strong muscles and bones.")
        print("If you are achieving this level of activity, then you should be fairly healthy! 😀")
    elif 18 <= age < 64:
        print("Since you are ", age," years old, you will need a minimum of 150 TO 300 minutes of moderate physical activity a day.", sep='')
        print("At least 2 days a week of light/moderate muscle training should provide you with the benefits you need to be healthy.")
        print("If you are achieving this level of activity, then you should be fairly healthy! 😀")
    elif 65 <= age:
        print("Since you are ", age," years old, as a Senior, you will need a minimum of 150 TO 300 minutes of moderate physical activity a day.", sep='')
        print("You should also include strength and balance training 2 - 3 times per week to protect yourself against falls.")
        print("If you are achieving this level of activity, then you should be fairly healthy! 😀")

    print("")
    print("How to get started with physical activity exercises: ")
    print("")
    print("When it is your first time exercising, you should never overdo it.")
    print("Start by trying something very light and pleasant like stretching or an easy walk, or dancing around to music you like!")
    print("Once you build yourself up from doing the light exercises, you can slowly start doing more moderate level exercises like jogging and weight lifting.")
    print("Everyone moves and progresses at their own pace, as long as you exercise a little bit each day, you will slowly but surely progress towards a healthy lifestyle.")
    print("Goodluck and remember to enjoy exercising! 😀")
    print("")

#Function 5
def RU_Nutritious(firstName, age, gender):
    print("")
    print("")
    print("Welcome to RU Nutritious!")
    print("This function provides you information on how much of each macronutrient you should be consuming daily, along with what even are macronutrients and what each macronutrient does for the body.")
    print("")
    while True:
        try:
            weight = int(input("Please enter your weight in pounds(lb): "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid weight.")

    kg = weight * 0.45359237
    kg = round(kg, 2)
    while True:
        try:
            height_feet = int(input("Please enter your height in feet: "))
            height_inches = int(input("Please enter your height in inches: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number for height.")

    height_inches = (height_feet*12) + height_inches
    height_feet = height_inches/12
    height_cm = height_feet * 30.48
    if gender == "male":
        bmr_constant = 5
    elif gender == "female":
        bmr_constant = -161
    bmr = 10 * kg + 6.25 * height_cm - 5 * age + bmr_constant
    calorie_calculation = round(bmr * 1.55)
    print("")
    print("Macronutrients are the nutrients we need in larger quantities that provide us with energy. These include Proteins, Fats, and Carbohydrates.")
    print("")
    print("The American Dietetic Association recommends daily protien intake for healthy adults as 0.8 - 1.0 g of protien per kg of body weight.")
    lowProtienEstimate = kg * 0.8
    lowProtienEstimate = round(lowProtienEstimate, 2)
    highProtienEstimate = kg * 1
    highProtienEstimate = round(highProtienEstimate, 2)
    print("Meaning that it is recommended that you eat ", lowProtienEstimate, " - ", highProtienEstimate, " grams of protien per day.",sep="")
    print("Consuming protein is incredibly important as protein intake builds and repairs muscles and bones.")
    print("Protein can also be used as an energy source for the body to use.")
    print("Examples of proteins are meat, fish, eggs, nuts, beans, etc.")
    print("")
    print("Daily Fat intake should equal 30% of the total calories you consume in one day.")
    print("Your daily average caloric intake is ", calorie_calculation, ".", sep="")
    daily_fat_calories = calorie_calculation * 0.3
    daily_fat_calories = round(daily_fat_calories, 2)
    fat_grams = daily_fat_calories/9
    fat_grams = round(fat_grams, 2)
    print("This means that you should consume ", daily_fat_calories, " calories of fat daily.", sep="")
    print("This can also be viewed as consuming ", fat_grams, " grams of fat per day.", sep="")
    print("Consuming fat is also very important as fat intake stores energy, and protects our vital organs.")
    print("By consuming fat you can lower the risk of developing heart disease, improve blood cholesterol levels, help with blood sugar control, and reduce inflammation.")
    print("Examples of fats are avocados, peanuts, salmon, cheese, pork, etc.")
    print("")
    print("The USDA recommends that 45 to 65 percent of your total daily calories should come from carbohydrates!")
    lowCarbEstimate = calorie_calculation * 0.45
    lowCarbEstimate = round(lowCarbEstimate, 2)
    highCarbEstimate = calorie_calculation * 0.65
    highCarbEstimate = round(highCarbEstimate, 2)
    print("This means that you should consume ", lowCarbEstimate, " - ", highCarbEstimate, " calories of carbohydrates daily.", sep='')
    print("Consuming carbohydrates is extremely important as they are your main source of energy!")
    print("Consuming carbs gives you energy throughout the day, and helps fuel your brain, kidneys, heart muscles, and central nervous system.")
    print("Examples of carbohydrates include bread, potatos, rice, donuts, cookies, milk, etc.")
    print("")


main()
print("Thank you for using our program ❤")
