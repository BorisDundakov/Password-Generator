# This program generates random 'n' digit passwords and stores them into a notepad file
import random
import string

n_digits = 8
lowercase_letters = string.ascii_lowercase
uppercase_letters = string.ascii_uppercase
numbers = string.digits
symbols = string.punctuation

all_chars = lowercase_letters + uppercase_letters + numbers + symbols

password = "".join(random.sample(all_chars, n_digits))

with open('passwords.txt', 'a', ) as f:
    f.write(f"{password}\n")
