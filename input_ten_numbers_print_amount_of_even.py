numbers = list(map(int, input("Enter 10 numbers:").split()))

even_number = len(list(filter(lambda num: num % 2 == 0, numbers)))
print(even_number)
