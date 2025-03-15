numbers = list(map(int, input("Enter 10 numbers: ").split()))

unique_numbers = []
for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)

print(unique_numbers)