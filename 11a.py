# d = "selamat"
# print(d.isalpha()) # diprint True jika input alfabet

# d = "selamat datang"
# print(d.isalpha()) # diprint False karena ada spasi (bukan alfabet)

# d = "5689"
# print(d.isdigit()) # diprint True jika input angka

# d = "56 89" 
# print(d.isalpha()) # diprint False karena ada spasi (bukan angka)

# d = "56.89" 
# print(d.isalpha()) # diprint False karena float (bukan integer)

# # print(int(d)) # ValueError
# print(int(56.89)) # 56

# e = "andi2589"
# print(e.isalnum()) # True jika alfabet (a - z) atau angka (0 - 9)

# e = "andi.2589"
# print(e.isalnum()) # False karena mengandung titik

# e = "andi 2589"
# print(e.isalnum()) # False karena mengandung spasi

# Jawaban latihan 10

## Nomor 1 dengan def dan return function
def calc(x,y,z):
    if z == "+":
        return x + y
    elif z =="-":
        return x - y
    elif z == "*":
        return x * y
    elif z == "/":
        return x / y
    else:
        return "Operator tidak tersedia"

try:
    angka1 = int(input("Masukkan angka : "))
    angka2 = int(input("Masukkan angka : "))
    simbol = input("Pilih operator (+, -, /, *): ")
    hasil = calc(angka1,angka2,simbol)
    print(f"Hasil {simbol} dari {angka1} dan {angka2} adalah {hasil}")
except:
    print("Hanya menerima bilangan integer")