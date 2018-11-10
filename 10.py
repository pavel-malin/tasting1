import random
psw = '' # предварительно создаем переменную psw
for x in range(12):
    psw = psw + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLXCVBNM'))

print(psw)
# Выведет: Ci7nU6343YGZ