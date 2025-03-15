num1 = int(input("Input number 1:"))
num2 = int(input("Input number 2:"))
if num1 > num2:
    num1, num2 = num2, num1

for num in range(num1 + 1, num2):
    print(num)

if num1 + 1 == num2:
    print("No numbers in between.")
