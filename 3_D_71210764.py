import random

tipe = str(input("Masukkan tipe yang ingin anda coba : "))

angka1 = random. randint(1, 20)
angka2 = random. randint(1, 20)
angka3 = random. randint(1, 20)
angka4 = random. randint(1, 20)

perbandingan = ['<','>','==']
hasil = random.choice(perbandingan)

benar = "benar" == True
salah = "salah" == False

def generateSoal():
    if tipe == str("penjumlahan"):
        print(f"(benar/salah) jika {angka1}+{angka2}{hasil}{angka3}+{angka4}")
    elif tipe == str("pengurangan") :
        print((f"(benar/salah) jika {angka1}-{angka2}{hasil}{angka3}-{angka4}"))

def cekHasil():
    jawaban = input("Maskkan Jawaban Anda : ")
    if (angka1+angka2,hasil,angka3+angka4) == True:
        print("Jawaban Anda Benar !")
    else:
        print("Jawaban Anda Masih Salah !")
    


generateSoal()
cekHasil()

