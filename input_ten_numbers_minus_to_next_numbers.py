numbers = list(map(int, input("Enter 10 numbers:").split()))

result = numbers[0]
for num in numbers[1:]:
    result -= num

print(result)
