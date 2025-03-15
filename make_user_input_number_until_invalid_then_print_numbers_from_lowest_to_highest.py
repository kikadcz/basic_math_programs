numbers = []

while True:
    try:
        numbers.append(float(input("Enter a number:")))
    except ValueError:
        break

if numbers:
    print("Numbers in order from lowest to highest:", sorted(numbers))
else:
    print("No numbers were entered.")
