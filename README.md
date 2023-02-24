
# Wordlist using python

In this project, you can generate unlimited passwords and save all passwords in a txt file.
let's start...............

To make this project you need to follow this step:-










## Installation

Install package with pip

```bash
  pip install more-itertools

```
    
## Deployment

To deploy this project run

```bash
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
```


## 







## You can follow me

Facebook:- https://www.facebook.com/problemsolvewithridoy/

Linkedin:- https://www.linkedin.com/in/ridoyhossain/

YouTube:- https://www.youtube.com/@problemsolvewithridoy

Gmail:- entridoy2@gmail.com

If you have any confusion, please feel free to contact me. Thank you

