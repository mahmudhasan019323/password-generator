#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

nr_letters= int((input("How many letters would you like in your password?\n") or 0)) 
nr_symbols = int((input("How many symbols would you like?\n") or 0))
nr_numbers = int((input("How many numbers would you like?\n") or 0))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
def weak_password(letter_count, symbol_count, number_count):
    password = ''
    for letter in range(letter_count):
        password += random.choice(letters)
    for symbol in range(symbol_count):
        password += random.choice(symbols)
    for number in range(number_count):
        password += random.choice(numbers)
    return password

print(f"The weak password is: {weak_password(nr_letters,nr_symbols,nr_numbers)}")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

def strong_password(letter_count, symbol_count, number_count):
    password_list = []
    password = ''
    for letter in range(letter_count):
        password_list.append(random.choice(letters))
    for symbol in range(symbol_count):
        password_list.append(random.choice(symbols))
    for number in range(number_count):
        password_list.append(random.choice(numbers))
    random.shuffle(password_list)
    for char in password_list:
        password += char
    return password

print(f"the strong password is: {strong_password(nr_letters,nr_symbols,nr_numbers)}")
