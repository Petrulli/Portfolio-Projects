def bmi(weight, height):
    result = weight/(height**2)
    return result

weight = int(input('what\'s your weight? '))
height = float(input('what\' your height? '))

bmiResult = bmi(weight, height)
print(bmiResult)

