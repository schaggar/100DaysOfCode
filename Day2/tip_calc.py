#total_amount = input("Enter the total bill:")

input_amount = input("Enter the total bill:")
input_members = int(input("Enter the number of persons:"))
input_tip = int(input("Enter the tip percentage i.e 10, 12 or 15:"))
converted_amount = float(input_amount.replace("$",''))

print(type(input_amount))
print(type(input_members))
print(type(input_tip))
print(type(converted_amount))

print((converted_amount/input_members))
split_pay = (converted_amount/input_members)*(input_tip/100)
print("Each member should pay:" + str(split_pay))