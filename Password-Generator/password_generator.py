import random

letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y','z']
number = ['0', '1', '2', '3', '4', '5', '6', '7','8', '9']
symbol = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("Welcome to the Password Generator!\n")
n_letters = int(input("How many letters would you like in your password?\n"))
n_number = int(input("How many numbers would you like in your password?\n"))
n_symbol = int(input("How many symbols would you like in your password?\n"))

password = []
for char in range(1, n_letters + 1):
  password += random.choice(letter)

for char in range(1, n_number +1):
  password += random.choice(number)

for char in range(1, n_symbol +1):
  password +=random.choice(symbol)

random.shuffle(password)
final_password = ""
for char in password:
  final_password += char

print(f"Your password is: {final_password}")


#By Nafiul Islam Santo.
