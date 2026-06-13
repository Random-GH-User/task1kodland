#modules

import random

#variables

characters = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
epl = ""
pass_storage = ""

#loop
while True:
    pass_storage = ""
    epl = int(input("Enter the length of the password: "))

    for i in range(epl):
        pass_storage += random.choice(characters)
    print(pass_storage)
