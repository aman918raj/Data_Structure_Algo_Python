num1 = 3
num2 = num1

print(f"num1 is : {num1}")
print(f"num2 is : {num2}")

print(f"num1 points to : {id(num1)}")
print(f"num2 points to : {id(num2)}")

num1 = 3
num2 = 4

print(f"num1 is : {num1}")
print(f"num2 is : {num2}")

print(f"num1 points to : {id(num1)}")
print(f"num2 points to : {id(num2)}")

num1 += 2

print(f"num1 is : {num1}")
print(f"num1 points to : {id(num1)}")
