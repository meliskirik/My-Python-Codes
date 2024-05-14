import random
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
symbols ="[]{}()*;/,._-"

all = upper + lower + numbers + symbols
length = random.randint(7,16)
print("Length: ", length)

password ="".join(random.sample(all,length))

print("Password: ", password)