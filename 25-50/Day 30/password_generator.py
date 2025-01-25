import random

def generate_password() :
  letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

  nr_letters = random.randint(5, 10)
  nr_symbols = random.randint(2, 5)
  nr_numbers = random.randint(2, 5)



  chars = [random.choice(letters) for letter in range(nr_letters)]
  symbol = [random.choice(symbols) for symb in range(nr_symbols)]
  number = [random.choice(symbols) for num in range(nr_symbols)]


  password_list = chars + symbol + number
  random.shuffle(password_list)

  password = "".join(password_list)
  return password

