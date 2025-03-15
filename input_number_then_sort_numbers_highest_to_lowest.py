numbers = []

while True:
    try:
        num = float(input("Enter a number:"))
        numbers.append(num)
    except ValueError:
        print("Invalid input. Stopping input.")
        break

if numbers:
    numbers.sort(reverse=True)
    print("Numbers from highest to lowest:", numbers)
else:
    print("No valid numbers were entered.")