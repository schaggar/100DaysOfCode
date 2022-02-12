height = float(input("Enter the height in cms:"))
weight = float(input("Enter the weight in kgs:"))
height_mt = height/100

bmi = int(weight/(height_mt ** 2))
print("Your BMI is:" + str(bmi))