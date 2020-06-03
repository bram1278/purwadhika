# string , number (integer, float, complex), boolean

# Untuk mengubah masukan perintah di Visual Studio Code menjadi comment atau sebaliknya, dapat menggunakan ctrl + /

print(5+5)

print("hello world")
print('hello world')
print('''hello world''')

# print('hari ini hari jum'at')
print("hari ini hari jum'at")
print('hari ini hari jum\'at')

nama = "Joni"
usia = 25
tinggi = 179.5

print(nama)
print("nama saya joni andre usia 25 tahun")
# print ("nama saya jo ni andre 
# usia 25 tahun")
print('''nama saya joni andre 
usia 25 tahun''')
print(type(tinggi))
print(type(usia))
print(type(nama))

print("nama saya : ", nama)
print("nama saya : " + nama)
# print("nama saya : " + usia) error karena di sebelah + harus string tidak boleh angka/integer
print("nama saya : " + "joni")
print("nama saya : " * 3)
print("usia saya : ", usia)
print("tinggi saya : ", tinggi)

print("nama saya :", nama, "usia saya : ", usia, "tinggi saya : ", tinggi)

usia2 = int("25") # mengubah string menjadi integer
print("usia saya : " + str(usia2) ) # str mengubah no-string menjadi string
print("nama saya : " + nama + " usia saya : " + str(usia2) + " tinggi saya : " + str(tinggi))

print("nama saya : {}, usia saya {}, tinggi saya {} ".format(nama,usia,tinggi))
print("nama saya : {2}, usia saya {1}, tinggi saya {0} ".format(nama,usia,tinggi)) # {2} {1} {0} mengubah urutan 
print("nama saya : %s usia saya %d, tinggi saya %f ".format(nama,usia,tinggi)) # %s string ; %d angka; %f float; % itu berurutan

print(f"nama saya : {nama} usia saya : {usia} tinggi saya {tinggi} ")

# nama
# Nama --> variabel adalah case sensitive
# _nama; _Nama; _Nama123 --> tanda _ dapat dikenakan kepada variabel

# nama = "Joni"
# nama = "Andre" --> sistem akan membaca variabel 'nama' dari "Joni" menjadi "Andre"

# nama = "Joni"
# nama = 24 --> dapat diubah dari string menjadi int

nama3 = "Andi Raharja"
print(len(nama3)) # spasi dihitung sebagai panjang (length) string

print(nama3.lower())
print(nama3.upper())
print(nama3.replace("a","i"))

print(nama3[0])

# [start : end : step] --> untuk mengakses index
# inclusive, exclusive 
print(nama3[1 : 4 : 1]) # inclusive dari 1, exclusive 4 karena index ke-4 tidak terhitung melainkan index ke-3
print(nama3[0 : 4])
print(nama3[-1]) # tanda -1 mengubah urutan penghitungan karakter string dari sebelumnya kiri ke kanan menjadi dari kanan ke kiri
print(nama3[10])
print(nama3[: 4])
print(nama3[::2])

print(nama3.index('R'))

print(nama3.split(" "))
print(nama3.split("R"))

nama4 = "Andi/Raharja/tinggal;jakarta"

print(nama4.split(" ")) # pemisah/pembagi adalah spasi
print(nama4.split("R")) # pemisah/pembagi adalah karakter huruf R

nama5 = input("Masukkan nama anda : ")
usia5 = input("Masukkan usia anda : ")

print("nama anda adalah : ",nama5, "Usia anda : ", usia5)
print("Usia anda 5 tahun mendatang adalah : ", int(usia5)+5)

usia6 = int(input("Masukkan usia anda : "))
print("Usia anda 5 tahun mendatang adalah : ", usia6+5)

print(5+5) # penjumlahan
print(5-5) # pengurangan
print(5/5) # pembagian
print(5*5) # perkalian
print(5%5) # sisa hasil bagi
print(7%5)

# inputnya : Nama, Usia, Pekerjaan, Gaji
# outputnya : nama, pekerjaan, usia 5 tahun yang lalu, gaji anda jika naik 2x lipat ....

# Nama = input("Masukkan nama anda :")
# Usia = int(input("Masukkan usia anda :"))
# Pekerjaan = input("Masukkan pekerjaan anda :")
# Gaji = int(input("Masukkan usia anda :"))
# print(f"nama saya adalah {}, usia saya ")

# Joni memiliki peternakan, dia beternak kambing dan ayam, jumlah nya 13, jumlah kaki nya 32
# berapa jumlah ayam dan berapa jumlah kambing?

# Soal 1
# Sembilan belas tahun yang lalu umur anak setengah tahun lebih muda dari seperempat umur ibunya.
# Umur anak sekarang 19 tahun lebih tua dari sepertujuh umur ibunya
# Output : Umur Ibu saat melahirkan anaknya

# Soal 2
# Jumlah umur andi dan umur ayahnya sekarang adalah 50 tahun.
# 4 tahun yang lalu umur ayah andi 6 kali umur andi.
# Output : Umur andi dan umur ayah saat ini adalah : ...

# email: khumaeni@purwadhika.com

print("Halo\nnama saya joni andre \npanggil saya joni") # \n untuk new line