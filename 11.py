## Function
## Digunakan untuk membuat fungsi yang akan dipakai berulang kali
## function pasti memiliki nama

## Syntax nya
# def namaFunction():
#     expressionnya / program

# Cara mendefinisikan/membuat function
def fungsi():
    print("Ini adalah contoh Fungsi sederhana")

# cara memanggil function
# fungsi()
# fungsi()
# fungsi()
# fungsi()

# Function di dalam function lain

def namaikan():
    print("Nama ikan ini adalah ikan gurame")

# namaikan()

def hargaikan():
    namaikan()
    print("Harga ikan gurame per ekor 80000")

# hargaikan()

# Membuat Function dengan argumen
# argumen adalah nilai/variabel yang ada setelah nama function di dalam tanda kurung
# jika ada nilai yang ingin kita gunakan di dalam function

def belanja(ekor):
    hargaikan()
    harga = 80000
    hargatotal = harga * ekor
    print(f"Harga ikan gurame {ekor} ekor adalah {hargatotal}")

# belanja(5)
# print(belanja(5)) # hasilnya none karena tidak ada return value

## Function dengan multiple argumen
def guru(nama, pelajaran):
    print(f"Nama guru ini {nama}")
    print(f"Mengajar pelajaran {pelajaran}")

# guru("Budi", "Sejarah")
# guru("Sejarah", "Budi") # ini contoh yang salah, memasukkan argumen harus berurutan sesuai yang ada pada function
# guru("Budi") # error karena jumlah argumen harus persis sama dengan yang ada pada function

## Memanfaatkan Keywords
# guru(nama="Budi", pelajaran="Sejarah") # ketika memanggil function dan memasukkan nilai argumen, menggunakan nama argumen(keywords) pada function
# guru(pelajaran="Sejarah", nama="Budi")

# Function menggunakan nilai Default
# def pegawai(nama, jabatan, gaji):
#     print(f"Nama pegawai ini adalah {nama}")
#     print(f"Memiliki jabatan {jabatan}")
#     print(f"Dan memiliki gaji {gaji}")

# pegawai("Eko") # error karena hanya memasukkkan 1 argumen sedangkan yang dibutuhkan 3

def pegawai(nama, jabatan="Staff", gaji=10000000): # Argumen yang tidak memiliki nilai default harus diisi valuenya ketika memanggil function
    print(f"Nama pegawai ini adalah {nama}")
    print(f"Memiliki jabatan {jabatan}")
    print(f"Dan memiliki gaji {gaji}")

# pegawai("Eko")
# pegawai(nama="Beni", jabatan="Data Engineer")
# pegawai(nama="Doni", jabatan="Developer", gaji=15000000)
# pegawai(jabatan="Supervisor", gaji=20000000) # error karena keyword nama tidak diset 

## Function dengan Return Value, kita gunakan ketika kita ingin mendapatkan hasil dari proses yang ada di dalam function
# def pangkat(x,y):
#     hasil = x ** y
#     print(f"nilai dari {x} pangkat {y} adalah {hasil}")

# a = pangkat(2,3)

# print(a) # Hasilnya none
# # print(print(20)) # nilai 20 diprint satu kali, setelah itu hasilnya none
# print(print(2*2))

# def pangkat(x,y):
#     hasil = x ** y
#     print(f"nilai dari {x} pangkat {y} adalah {hasil}")
#     return hasil

# a = pangkat(2,3)

# print(a) # diprint hasil 2 pangkat 3

# bentuk common dari return value
# def pangkat2(x):
#     hasil = x ** 2
#     return hasil

# b = pangkat2(4) 
# print(b) # diprint hasil 4 pangkat 2

# def pangkat2(x):
#     hasil = x ** 2
#     return [2, 7, 8]

# b = pangkat2(7)
# print(b) # hasilnya [2, 7, 8]
# b = pangkat2(10) 
# print(b) # hasilnya [2, 7, 8]

# def pangkat2(x):
#     hasil = x ** 2
#     a = True
#     kata = "Ini kalimat"
#     return a

# b = pangkat2(7)
# print(b) # diprint True

# def pangkat2(x):
#     hasil = x ** 2
#     a = True
#     kata = "Ini kalimat"
#     return kata

# b = pangkat2(7)
# print(b) # diprint "Ini kalimat"

def pangkat2(x):
    hasil = x ** 2
    a = True
    kata = "Ini kalimat"
    return hasil # penentuan value yang akan direturn sangat penting

b = pangkat2(86)
# print(b)

def perkalian(x,y):
    hasil = x * y # local variable
    return hasil

# c = perkalian(10, 5) # diprint hasil 10 kali 5
# print(c)

c = perkalian(10, pangkat2(5))

# print(perkalian(10, pangkat2(5)))

# =========================================

# Anonymous Funtion (fungsi tanpa nama) : Lambda
# Anonim, fungsi sekali pakai, ukurannya kecil (fungsinya sedikit)
# tidak dapat mereturn value (bentuknya berbeda)

# Syntax nya
# lambda arguments : expression programnya # lambda harus punya argumen, tidak bisa tidak punya. Lambda bisa memiliki banyak argumen, expression (programnya) cuma bisa 1

def tambah(x, y):
    return x + y

# print(tambah(2, 5)) # diprint 2 tambah 7

# lambda

def kuadrat(x):
    return x ** 2

# print(kuadrat(5))

power = lambda x: x ** 2
power(5)
# print(type(kuadrat))
# print(type(power)) # power memiliki class bertipe function
# print(power(5))

jumlah = lambda x, y: x + y

# print(tambah(2,8)) # print 2 tambah 8
# print(jumlah(5, 5))

ops = lambda a, b, c: a + b * c
# print(ops(2,5,6)) # diprint 2 + 5 * 6

def myfunc(x):
    return lambda a: a ** x

# print(myfunc(4)) # keluar function myfunc.<locals>.<lambda>

pangkat2 = myfunc(2) # nilai x adalah 2
pangkat3 = myfunc(3) # nilai x adalah 3

# print(pangkat2(3)) # 3 di sini adalah nilai a, sehingga diprint 3 pangkat 2

# print(pangkat3(2)) # 2 di sini adalah nilai a

def myfunction(z):
    return lambda b: b * z

dobel = myfunction(2) # nilai z adalah 2
triple = myfunction(3) # nilai z adalah 3

# print(dobel(11)) # 11 adalah nilai b
# print(triple(11)) # 11 adalah nilai b

### Map
## Function, mirip seperti lambda (anonymous function)
# Syntax
# map(function, data iterables) # Data iterable : list, dict, dll (mengandung banyak data)
# jumlah data iterables (argumen), tergantung pada jumlah argumen pada functionnya

a = [2, 3, 4, 5]
def kali(x):
    return x * 2

# cara 1
for i in a:
    print(kali(i))

# cara 2 dengan map
# print(map(kali, a))
# b = map(kali, a) 
# print(b) # ada keterangan <map object at ...>
b = list(map(kali, a)) 
print(b) # ada keterangan <map object at ...>

# map dengan lambda
c = list(map(lambda x: x * 2, a))

print(c)

a = [1, 2, 3]
b = [10, 20, 30]

d = list(map(lambda x, y: x + y, a, b)) # nilai x dan y didapat dari list a dan b
print(d)

e = list(map(lambda x: x ** 2, b)) # isi list b dipangkat 2
print(e)

### Filter (mirip map dan lambda)
# Syntax
# filter(function, data iterables) === Sejenis fungsi Boolean, tetapi hanya mengembalikan nilai/value yang bernilai True
# filter hanya bisa menerima 1 data iterable

s = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

d = []
for i in s:
    if i%2 == 0:
        d.append(i)
print(d)

# result = filter(lambda x: x%2==0,s)
# print(result) # mendapat notif <filter object at ...>
result = list(filter(lambda x: x%2==0,s))
print(result) # diprint angka genap

result = list(filter(lambda x: x%2!=0,s))
print(result) # diprint angka ganjil

res = list(filter(lambda a: a > 6, s))
print(res) # diprint angka lebih besar dari 6

# Lat 1:
# Buat algoritma ---
# buat List
# Pilihan:
# 1 = ascending (a - z) dari kecil ke besar
# 2 = descending(z - a) dari yang terbesar ke terkecil
# reverse, ::-1
# Output: sesuai Pilihan

# # Lat 2
# Buat algoritma
# cari nilai maksimal dan nilai minimal

# # Lat 3
# Buat algoritma
# Buat list
# cari :
# Modus : nilai yang paling sering muncul
# Median : Nilai tengah
# Mean : rata-rata
# Q1 : Quartal 1 atau 25 %
# Q3 : Quartal 3 atau 75 %
# Outliers

# Latihan 4
# Buat def atau function
# Ada deret angka
# 1 2 3 4 5
# 6 7 8 9 10
# 11 12 13 14 15
# 16 17 18 19 20
# 21 22 23 24 25

# input : Spin ke : pilihan 1-4
# outputnya
# pilihan 1:
# 21 16 11 6 1
# 22 17 12 7 2
# 23 18 13 8 3
# 24 19 14 9 4
# 25 20 15 10 5

#pilihan 2:
# 25 24 23 22 21 
# 20 19 18 17 16
# 15 14 13 12 11
# 10 9 8 7 6
# 5 4 3 2 1

# pilihan 3:
# 5 10 15 20 25
# 4 9 14 19 24
# 3 8 13 18 23 
# 2 7 12 17 22
# 1 6 11 16 21

# pilihan 4
# 1 2 3 4 5
# 6 7 8 9 10
# 11 12 13 14 15
# 16 17 18 19 20
# 21 22 23 24 25