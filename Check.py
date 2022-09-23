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
        LBs_to_KGs = weight / 2.2
        FT_to_CM = height * 30.48
        CM_to_M = FT_to_CM * 0.01
        M2 = CM_to_M ** 2
        var = LBs_to_KGs / M2
        return f'Your current BMI is {round(var, 2)}.'


name = str(input("What's your name? "))
age = int(input("How old are you? "))
weight = float(input("What's your weight? Lbs "))
height = float(input("What's your height? Feets "))
gender = str(input("What's your gender? male/female "))

clnt = Profile(name, age, weight, height, gender)
print(repr(clnt))
print(Nutrition_detailed.BMI())