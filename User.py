import random
import string
length = int(input("Enter password length: "))
use_letters = input("Include letters? (y/n): ").lower() == 'y'
use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

charset = ""
if use_letters:
    charset += string.ascii_letters   # a-zA-Z
if use_numbers:
    charset += string.digits          # 0-9
if use_symbols:
    charset += string.punctuation     # Special characters
if not charset:
    raise ValueError("At least one character type must be selected!")

password = ''.join(random.choice(charset) for _ in range(length))
print("Generated password:", password)

