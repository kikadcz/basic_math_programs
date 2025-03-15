numbers = []

user_input = input("Enter a number (or any non-numeric value to stop): ").strip()

while user_input.replace('.', '', 1).isdigit():
    numbers.append(float(user_input))
    user_input = input("Enter a number (or any non-numeric value to stop): ").strip()

if numbers:
    average = sum(numbers) / len(numbers)
    print("Average of entered numbers:", average)
else:
    print("No valid numbers were entered.")
