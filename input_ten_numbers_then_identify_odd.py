numbers = list(map(int, input("Enter 10 numbers:").split()))

odd_number = len(list(filter(lambda num: num % 2 != 0, numbers)))
print(odd_number)
