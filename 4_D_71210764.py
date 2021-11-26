import random

def tabakangka():
    ran = random.randint(1, 10)
    print(f"Apakah {ran}?")
    return ran

x = int(input("Untuk memulai program masukkan (-1) untuk mulai : "))

if x == -1:
    tabakangka()
elif x != -1 :
    print("Masukkan ulang!")