import random
import time

def numero_aleatorio ():
    num = random.randint(1,10)
    print(num)
    with open("numero.txt", "a") as file:
        file.write(f"{num}\n")


if __name__ == "__main__":
    while True:
        num = numero_aleatorio()
        time.sleep(1)