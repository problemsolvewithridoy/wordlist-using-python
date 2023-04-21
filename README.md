
# Wordlist using python

The "Wordlist using python" project is a Python script that generates a list of words that can be used for various purposes, such as password cracking, dictionary attacks, or brute-force attacks. The script is designed to generate a wordlist based on user-specified parameters, such as word length, character set, and prefix/suffix options. The generated wordlist can be saved in a text file for future use.

The script is written in Python programming language and uses built-in Python libraries such as itertools and string. It is a beginner-friendly project that can be useful for anyone interested in learning Python programming and ethical hacking techniques. The project can also be extended to add more features, such as custom wordlists or advanced pattern matching algorithms. The code is available on Github and can be easily downloaded and customized to meet specific requirements.

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

