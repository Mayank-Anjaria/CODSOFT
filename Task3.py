# Task 3 Password Generator

import random
import string

def generate(length):

    characters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(characters) for i in range(length))
    return password

length = int(input("\nEnter the length of the password : "))

password = generate(length)
print("\nGenerated Password : ", password)