# Fungsi

karakter = str(input("Masukkan sebuah kata/kalimat : "))
sisip = str(input("Masukkan karakter yang ingin disisipkan :  "))

def sisipHuruf():
    print(sisip.join(karakter.upper()))

def sisipKata() :
    print(sisip.join(karakter.split()))

sisipHuruf()
sisipKata()

