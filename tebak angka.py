import random
def tebak_angka():
    secret_number = random.randint(1, 67)
    tebakan = 0
    nyoba = 3

    print("gas tebak angka 1-67")
   
    while tebakan != secret_number:
        try:
            tebakan = int(input("masukan angka:"))
            nyoba -= 1

            if tebakan < secret_number:
                print("kekecilan")
            elif tebakan > secret_number:
                print("kebesaran")
            else:
                print(f"hoki {secret_number} adalah angka yang benar")
                break
            if nyoba == 0:
                print(f"maaf kesempatan habis, angka yang benar adalah {secret_number}")
                break
        except ValueError:
            print("input tidak valid, coba lagi")
            continue
if __name__ == "__main__":
    tebak_angka()
