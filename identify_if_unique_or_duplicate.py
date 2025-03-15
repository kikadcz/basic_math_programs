numbers = []

while True:
    try:
        num = float(input("Enter a number:"))

        if num in numbers:
            print("Duplicate")
        else:
            print("Unique")
        numbers.append(num)

    except ValueError:
        break

print("All entered numbers:", numbers)