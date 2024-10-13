import random

simvol = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
line = int(input("введите длину пароля:\n"))
password = ""

for a in range(line):
    password += random.choice(simvol)

print(f'ваш пароль - {password}')