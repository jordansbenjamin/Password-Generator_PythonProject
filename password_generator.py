import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

total_num_of_password = nr_letters + nr_numbers + nr_symbols

password = ""

length_letters = len(letters)
length_numbers = len(numbers)
length_symbols = len(symbols)

lst = [-1, -1, -1, -1, -1, -1]

count_letters, count_numbers, count_symbols = 0, 0, 0

for letter in range(nr_letters):
    if nr_letters > 0:
        random_letters = random.randint(0, length_letters - 1)
        password += letters[random_letters]

for symbol in range(nr_symbols):
    if nr_symbols > 0:
        random_symbols = random.randint(0, length_symbols - 1)
        password += symbols[random_symbols]

for number in range(nr_numbers):
    if nr_numbers > 0:
        random_numbers = random.randint(0, length_numbers - 1)
        password += numbers[random_numbers]

list_password = list(password)

random.shuffle(list_password)

# print(list_password)

password = ''.join(str(i) for i in list_password)

print(f"Your password is: {password}")





