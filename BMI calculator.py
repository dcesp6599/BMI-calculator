class Profile:
    def __init__(self, name, age, weight, height, gender):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height
        self.gender = gender
        if gender == "male" or "female":
            gender == gender
        else:
            print("Type... male or female please.")
    
    def __repr__(self):
        return f'Hi, {name}. You said, you are {age} years old. You are {int(weight)} lbs and {round(height, 2)} feet tall. Also, you are {gender}.'

class Nutrition_detailed(Profile):
    def __init__(self, height, weight):
        super().__init__(weight, height)
    
    def BMI():
        weight_convert = weight * 0.45
        height_convert = height * 0.30
        result = weight_convert / height_convert
        result1 = result / height_convert
        if result1 > 0 and result1 <= 18.5:
            category = "underweight"
        elif result1 > 18.5 and result1 <= 25:
            category = "healthy"
        elif result1 > 25 and result1 <= 30:
            category = "overweight"
        else:
            category = "obese"

        return f'Your BMI is {round(result1, 2)}. You fell under the {category} category.'


name = str(input("What's your name? "))
age = int(input("How old are you? "))
weight = float(input("What's your weight? Lbs "))
height = float(input("What's your height? Feets "))
gender = str(input("What's your gender? male/female "))

clnt = Profile(name, age, weight, height, gender)
print(repr(clnt))
print(Nutrition_detailed.BMI())