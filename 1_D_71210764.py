
string = float(input("Masukkan String : "))

def cekString():
    
    if string % 2 == 0  :
         print(int(string/2))

    elif (string % 2 != 0) :
         print(int((string + 5)/2))



cekString()
