min_num = None

while True:
    user_input = input("Enter a number (or press Enter to stop): ").strip()

    try:
        num = float(user_input)
        min_num = num if min_num is None or num < min_num else min_num
    except ValueError:
        print("Invalid input.")
        break

if min_num is not None:
    print(f"The lowest number entered was: {min_num}")
else:
    print("No valid numbers were entered.")
