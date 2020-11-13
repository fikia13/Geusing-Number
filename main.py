import random;

inputUser = int(input("Masukkan angka yang akan ditebak 1 - 10 "))
value = random.randrange(1,10,1)
if inputUser == value:
    print("tebakan anda benar")
elif inputUser > value:
    print("inputan anda terlalu besar")
else:
    print("inputan anda terlalu kecil ")