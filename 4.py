# try :
#   program
# except : 
#    program
# try dan except digunakan untuk menghandle error

try :
    angka = int(input("Masukkan angka : "))
except :
    print("Nilai yang anda masukkan salah")

else:
    if angka%2 == 0:
        print("Genap")
    else:
        print("Ganjil")
# .isdigit()
# .islower()
# .isupper()

# List = Data Structured
hari = ["senin", "selasa", "rabu", "kamis", "jum'at", "sabtu", "minggu"]
angka = [1,2,3]

print(*hari, sep='\n') # memprint semua isi dari list hari dan dipisahkan ke dalam separator \n (baris baru)

angka2 = [8,1,5,9,10,58,2]
angka2.sort() # mengurutkan nilai dari list; sort juga bisa digunakan untuk mengurutkan alfabet
print(angka2)
angka2.reverse() # membalik urutan dimulai dari nilai index yang paling akhir 
print(angka2)

print(hari)
print(hari[::-1]) # membalikkan urutan hari dari list "hari" dimulai dari paling belakang, minggu, sabtu, dst ...
print(hari)
hari.reverse() # membalikkan urutan hari dari list "hari" dimulai dari paling belakang, minggu, sabtu, dst ...
print(hari)

# angka2.clear() # clear menghapus seluruh isi dari list
# print(angka2)

angka2.sort()
print(angka2)

# angka2[0:2] = [70,90] # menambahkan nilai 70 dan 90 kepada index ke-0 dan ke-1
# print(angka2)

# mengurutkan
angka3 = angka2.copy # angka3 akan mengkopi nilai dari angka2

print(angka3) 

hari.append(angka2)
print(hari)
print(hari[7][4])
# akses list
# print(hari[0]) # print hari senin
# rint(hari[2]) # print hari rabu
# print(hari[-2]) # print hari sabtu karena dua dari belakang
# print(hari)
# print(hari[4])

nama = list("namaku andi")
print(nama)

Nama = "namaku andre"
print(Nama.split(" "))

Nama = "namaku_andre@gmail.com"
print(Nama.split("@"))

# Slicing

# Index 
# [start : end : step]

# [start : end] #step menggunakan default 1
# [inclusive: exclusive] # start bersifat inclusive, end bersifat exclusive

# print(hari[0:4])
# print(hari[2:4])
# print(hari[:])
# print(hari)
# print(hari[:4])
# print(hari[4:])

# menggabungkan dua atau lebih list
# hari.append(angka) # nilai data "angka" dijadikan satu list
# print(hari)

# print(hari + angka)

# hari.extend(angka)
# print(hari)

# menambahkan data
# hari.append("monday")
# hari.extend("sunday")

# print(hari)

# hari.insert(1,"tuesday")
# print(hari)

# hari[1]= "selasa2"
# print(hari)

# hari.remove("selasa2") # digunakan bila kita tahu nama/nilai data yang ingin dihapus
# print(hari)

# hari.pop() # nilai plaing akhir dari list hari dihapus
# print(hari)

# hari.pop(7) # nilai ke-7 pada list hari dihapus
# print(hari)

# print(hari.index("sabtu")) # print index ke berapakah nilai "sabtu" itu

print("a" in "halo dunia")

hari = ["senin", "selasa", "rabu", "kamis", "jum'at", "sabtu", "minggu"]
print(len(hari))

angka = [8,1,5,9,10,58,2]
print(max(angka))
print(min(angka))
print(sum(angka))
print(angka.count(10)) 

angka2 = angka * 2

print(angka2)

# minuman = [["Kopi", "Susu", "Teh"], ["Jus Apel","Jus Melon","Jus Jeruk"], ["Es Kopi", "Es Campur","Es Teler"]]

# print(minuman[1][3][1])

# tuple, imutable list
angka3 = (8,1,5,9,10,5,58,2) # gunakan tanda kurung biasa
angka4 = tuple(angka)

print(angka3.index(10))
print(angka3)
print(angka4)

# angka4.append(4) # error karena isi tuple tidak bisa ditambahkan
# print(angka4) 

# angka4.pop() # error karena isi tuple tidak bisa dikurang
# print(angka4)

# angka4.remove(10) # error karena tuple tidak bisa di=remove
angka3 = list(angka3)
angka3.remove(10)
print(angka3)
angka3 = tuple(angka3)
print(angka3)

angka3 = (8,1,5,9,10,5,58,2,(2,5,6,(5,78)))
print(angka3[2])
print(angka3[8][3][1])

var = ("Joni", 22, "bandung")
print(var)

nama, usia, kota = var

print(usia)
print(kota)

# kalimat = kalimat2[:] # jadi 2 variabel yang berbeda

# Latihan 1
# input : masukkan nama hari : SENIN atau selasA
# pengecekan input : "Tidak ada nama hari" lalu program di-close
#         jumlah : input hari yang diinginkan, cth: 100 hari atau -2 hari 
# output : (jumlah)hari dari sekarang adalah hari ....

# Latihan 2
# palindrome; contoh kata katak kalau dibalik katak juga

# input : masukkan kata
# kondisi : dilakukan pengecekan kata
# output : kata tersebut termasuk/bukan palindrome

# Latihan 3
# masukkan kalimat : "hari ini hari selasa"
# ada 2 pilihan (opsi 1 dan opsi 2)
# opsi 1. masukkan karakter : "a"
# outputnya : hri ini hri sels (menghapus huruf "a")
# opsi 2. masukkan karakter vokal : "o"
# outputnya : horo ono horo soloso (semua huruf vokal diganti menjadi huruf "o")

# Latihan 4
# (hanya menggunakan metode numerikal)
# Masukkan 4 digit angka : 5689 
# outputnya : 8956
# jika angka yang dimasukkan berupa string kata, keluar output : "Angka yang anda masukkan salah"

# Latihan 5
# (hanya menggunakan metode numerikal)
# input: masukkan angka 2 digit : 85
# masukkan 2 digit kedua : 32
# outputnya : 8532
# jika angka yang dimasukkan berupa string kata, keluar output : "Angka yang anda masukkan salah"