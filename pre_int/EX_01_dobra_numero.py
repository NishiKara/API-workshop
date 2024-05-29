import time


def dobra_um_numero(num):
    return num * 2 

def ler_ultimo_numero():
    try:
        with open("numero.txt", "r") as file: 
            lines = file.readlines()
            if lines:
                return int(lines[-1].strip())
            else:
                print("arquivo vazio.")
                return None
    except FileExistsError:
        print("arquivo não encontrado.")
        return None

if __name__ == "__main__":
    while True:
        num = ler_ultimo_numero()
        if num is not None:
            resultado = dobra_um_numero(num)
            print(f"o dobro do último numero {num} é {resultado}\n")
            time.sleep(1)