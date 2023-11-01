# solution 1:
#I have written the code in such a manner that, it will prompt the user to give input. 
#Based on the input it will execute.
# Actually it will basically search for max consecutive 4 digits and do the operation. 

# Enter a string: asd4563dfr9876
# Result is: 1088640  # 6 * 5 * 4 * 3 * 9 * 8 * 7 * 6 = 1088640

# anomaly Enter a string: 1234a3456b9876

# Enter a string: a1234v4567b9876
# Result is: 60963840  # 4 * 3 * 2 * 1 * 7 * 6 * 5 * 4 * 9 * 8 * 7 * 6 = 60963840


def max_multiplication(input_string):
    consecutive_digits = ""  # To store consecutive digits
    result = 1  # Initialize the result to 1
    stored_numbers = []  # To store the individual numbers contributing to the product

    for char in input_string:
        if char.isdigit():
            consecutive_digits += char
        else:
            if len(consecutive_digits) >3:
                # Sort the consecutive digits and keep the highest four
                sorted_digits = sorted(consecutive_digits, reverse=True)
                highest_four = sorted_digits[:4]

                product = 1
                for digit in highest_four:
                    int_digit = int(digit)
                    product *= int_digit
                    stored_numbers.append(int_digit)  # Store individual number
                result *= product
            consecutive_digits = ""  # Reset if a non-digit character is encountered
    if result == 1:
        return "nil", []  # Return "nil" and an empty list if no consecutive digits are found
    else:
        return result, stored_numbers

# Get input from the user
user_input = input("Enter a string: ")
result, stored_numbers = max_multiplication(user_input+" ")

if result != "nil":
    numbers_str = ' * '.join(str(num) for num in stored_numbers)
    print(f"Result is: {result}  # {numbers_str} = {result}")
else:
    print("nil.")