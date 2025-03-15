numbers = []

while True:
    try:
        num = int(input("Enter a number: "))
        numbers.append(num)
    except ValueError:
        break

if numbers:
    number_counts = {}

    for num in numbers:
        number_counts[num] = number_counts.get(num, 0) + 1

    most_frequent = max(number_counts, key=number_counts.get)

    print("Most frequent number:", most_frequent)
else:
    print("No numbers were entered.")
