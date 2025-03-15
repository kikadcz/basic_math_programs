numbers = list(map(int, input("Enter 10 numbers: ").split()))

duplicate_numbers = list(set([num for num in numbers if numbers.count(num) > 1]))

print("Duplicate numbers:", duplicate_numbers)