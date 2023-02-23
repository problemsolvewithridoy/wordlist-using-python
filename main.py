from string import *
from itertools import product

value = ascii_letters + digits + punctuation

count = 0

for i in range(3,4):
    for j in product(value, repeat = i):
        count += 1
        word = "".join(j)
        f = open("YourFileName.txt", "a")
        try:
            f.write(word)
            f.write("\n")
            print(f"\r{count} password created", end= "")
            if len(word) == 5:
                break
        except:
            print("can't able to create password")


print(f"{count} password is created")