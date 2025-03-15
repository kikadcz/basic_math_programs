max_num = None

while True:
    user_input = input("Enter a number (or press Enter to stop): ").strip()

    try:
        num = float(user_input)
        max_num = num if max_num is None or num > max_num else max_num
    except ValueError:
        print("Invalid input.")
        break

if max_num is not None:
    print(f"The highest number entered was: {max_num}")
else:
    print("No valid numbers were entered.")
