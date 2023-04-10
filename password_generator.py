import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = ""

length_letters = len(letters)
length_numbers = len(numbers)
length_symbols = len(symbols)

for letter in range(nr_letters):
    random_letters = random.randint(0, length_letters - 1)
    password += letters[random_letters]

for number in range(nr_numbers):
    random_numbers = random.randint(0, length_numbers - 1)
    password += numbers[random_numbers]

for symbol in range(nr_symbols):
    random_symbols = random.randint(0, length_symbols - 1)
    password += symbols[random_symbols]

print(password)





