#Sorted()
# iterable: The iterable to be sorted.
# key: An optional function that defines a custom sorting key. If specified, the key function is applied to each element in the iterable to determine the sort order. The elements are sorted based on the values returned by the key function.
# reverse: An optional boolean value that, when set to True, sorts the iterable in descending order (i.e., reverse order). By default, it is False.

# Function to convert a decimal number to binary
def decimal_to_binary(decimal_number):
    binary_representation = ""
    if decimal_number == 0:
        binary_representation = "0"
    else:
        while decimal_number > 0:
            remainder = decimal_number % 2
            binary_representation = str(remainder) + binary_representation
            decimal_number = decimal_number // 2
    return binary_representation

# Function to get the count of 1s in a binary number
def count_ones(binary_string):
    return binary_string.count('1')

# Input the size of the array
array_size = int(input("Enter the size of the array: "))

# Initialize an empty list to store the binary representations
binary_array = []

# Input the decimal numbers and convert them to binary
for i in range(array_size):
    decimal_number = int(input(f"Enter decimal number {i + 1}: "))
    binary_representation = decimal_to_binary(decimal_number)
    binary_array.append(binary_representation)

# Create a dictionary to store the counts
counts = {}

# Loop through the binary numbers and count '1's
for binary_number in binary_array:
    count = count_ones(binary_number)
    counts[binary_number] = count

# Sort the binary numbers based on the counts and then the decimal values
def custom_sort_key(item):
    binary_string, decimal_number = item
    return (counts[binary_string], decimal_number)

sorted_binary_numbers = sorted(zip(binary_array, [int(binary, 2) for binary in binary_array]), key=custom_sort_key)

# Print the sorted binary numbers in decimal format
for _, decimal_number in sorted_binary_numbers:
    print(decimal_number)

# The line binary_string, decimal_number = item is a form of unpacking in Python. In this context, item is a tuple containing two elements, and this line is used to extract those two elements and assign them to the variables binary_string and decimal_number.
# Here's how it works:
# item is a tuple containing two values, where the first value is the binary representation of a number (as a string), and the second value is the decimal representation of the same number.
# binary_string, decimal_number is a tuple unpacking statement. It matches the structure of the item tuple, so the first element of the tuple (binary_string) receives the first value from item, and the second element of the tuple (decimal_number) receives the second value from item.
# In the context of your code, item represents a pair of binary and decimal representations of numbers. By unpacking item, you make it easier to work with these two values separately within the sorting function and the subsequent code.
        

# In the provided code, item is defined in the context of the sorted function when you use the zip function to combine two lists: binary_array and a list of corresponding decimal numbers.
# Here's the relevant part of the code:
# sorted_binary_numbers = sorted(zip(binary_array, [int(binary, 2) for binary in binary_array]), key=custom_sort_key)
# The zip function takes two or more sequences (in this case, binary_array and [int(binary, 2) for binary in binary_array]) and pairs their elements together. In this case, it pairs each binary string from binary_array with the corresponding decimal number (converted from the binary string) and creates a list of tuples. Each tuple in the resulting list has two values: the binary string and the decimal number.
# So, when you iterate through sorted_binary_numbers, each item is a tuple with two values: the binary string and the decimal number. The line binary_string, decimal_number = item unpacks this tuple into two separate variables for easier access in the code that follows.






# [('1000', 8), ('11', 3), ('1001', 9), ('111', 7)]
# The structure you've provided is a list of tuples in Python. Each element in the list is a tuple containing two values. Tuples are ordered collections of elements, and in your case, each tuple consists of a binary string and its corresponding decimal number. Here's a breakdown of your example:
# ('1000', 8) is a tuple where the first element '1000' is a binary string, and the second element 8 is its corresponding decimal number.
# ('11', 3) is another tuple with a binary string '11' and a decimal number 3.
# ('1001', 9) is a tuple with a binary string '1001' and a decimal number 9.
# ('111', 7) is a tuple with a binary string '111' and a decimal number 7.
# You can access and manipulate the elements within these tuples just like you would with any other data structure in Python. For example, you can iterate through the list, access individual tuples, and then access the elements within each tuple as needed.





