import random
import string
n=int(input("Enter the length of the password: "))
characters=string.ascii_letters+string.digits+string.punctuation
password=""
for i in range(n):
    password+=random.choice(characters)
print("Your password is: ",password)