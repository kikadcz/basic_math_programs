numbers = list(map(int, input("Enter 10 numbers:").split()))

unique_numbers = [num for num in numbers if numbers.count(num) == 1]

print(unique_numbers)



