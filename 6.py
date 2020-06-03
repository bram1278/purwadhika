## Looping
## For Loop
## While Loop

## membership operator
## in
## not in dan !=

## identity operator
## is not dan !=
## is dan ==

# print(5 == 5)
# print(5 != 5)

# print(5 is 5)
# print(5 is not 5) # penggunaan is dan is not dapat dilakukan tetapi ada Syntaxwarning

# print(type(5) is int)
# print(type(5) is not int) # penggunaan demikian tidak mendapat Syntaxwarning

#### For
# angka = 6
# for i in angka : # penggunaan in harus banyak data, tidak bisa hanya satu saja
#     print(i) # Not iterable karena data harus lebih dari 1

# For menggunakan List    
buah = ["anggur", "kiwi", "apel", "jeruk", "pisang"]

for i in buah:
    print(i)

### For menggunakan Range angka

# range(start : end : step)
# (inclusive : exclusive)
print(type(range(10)))
print(range(10)) # defaultnya 10 merupakan end dan dimulai dari 0
print(range(0,10,1))

for i in range(10):
    print(i)
print("=" * 100)
for i in range(0,10,1):
    print(i)

# for i in range(51,10): # error karena tidak mungkin start dari 51 dan end pada 9
#     print(i)
print("=" * 100)
for i in range(0,51,10):
    print(i)

print("=" * 100)
for j in range(1,11): # range membaca dimulai dari 1 berakhir di 10
    if j%2 == 0:
        print('Genap')
    else:
        print(j)

### Break
for i in range(16):
    print(i)
    if i == 10:
        print("batas maksimal")
        break # proses looping dihentikan
        # print("Lanjut") # Tidak dijalankan karena looping sudah dihentikan

print("perintah di luar looping")

### For ... Else
angka = 5
for i in range(11):
    print(i)
    if i == angka:
        print("Data Ditemukan")
        break
    else:
        print("Data Tidak Ditemukan")

print("perintah di luar looping")

angka = 5
for i in range(11):
    print(i)
    if i == angka:
        print("Data Ditemukan")
        break
else:
    print("Data Tidak Ditemukan")

print("perintah di luar looping")

angka = 14
for i in range(11):
    print(i)
    if i == angka:
        print("Data Ditemukan")
        break
else:
    print("Data Tidak Ditemukan")

print("perintah di luar looping")

buah = ["anggur", "kiwi", "apel", "jeruk", "pisang"]
cari = "jeruk"

for i in buah:
    print(i)
    if i == cari:
        print("Data Ditemukan")
        break
else:
    print("Data Tidak Ditemukan")
# "pisang" tidak di-print karena perintah break sudah dijalankan sehingga looping stop
print("perintah di luar looping")

### Continue
for i in range(11):
    print(i)
    if i == 5:
        print('OK')
        continue # Proses iterasi dioper ke proses for yang pertama
    print("angka : ", i)

print("perintah di luar looping")

for i in range(11):
    print(i)
    if i == 5:
        print('OK')
        break
    print("angka : ", i)

print("perintah di luar looping")
print("=" * 100)

for i in range(11):
    
    if i == 5:
        print('OK')
        break
    print(i) # jika perintah print(i) dipindahkan ke setelah break
    print("angka : ", i)

print("perintah di luar looping")
print("=" * 100)

for i in range(11):
    
    if i == 5:
        print('OK')
        continue
    print(i) # jika perintah print(i) dipindahkan ke setelah continue
    print("angka : ", i)

print("perintah di luar looping")

### Nested For (For  di dalam For)
buah = ["anggur", "kiwi", "apel", "jeruk", "pisang"]
sayuran = ["wortel", "bayam", "terong", "kangkung", "mentimun"]
makanan = ["soto", "sate", "bakso", "rawon", "gulai"]

data = [buah, sayuran, makanan]
# print(data) # hasilnya ada list di dalam list

for jenis in data: # yang diakses adalah barisnya, cth: anggur, kiwi, apel, ...
    print(jenis)

    for j in jenis: # yang diakses adalah kolomnya , cth: anggur, wortel, soto
        print(j) # Hasil akan diprint berdasarkan list

print("perintah di luar looping")

for jenis in data:
    print(jenis)
    for j in jenis:
        print(j)

# for i in range(5):
#    for j in range(5,10):
#        print(j)

# for i in range(5):
#    for j in range(5,10):
#        pass

# for i in range(10):
#    pass

for huruf in "makanan":
    print(huruf)

list
# A = himpunan bilangan genap dari 1 - 20

# B = himpunan bilangan ganjil dari 1 - 20

# C = himpunan bilangan negatif lebih dari -20

# D = himpunan bilangan prima dari 1 - 20

# E = himpunan bilangan komposit dari 1 - 20

# F = A dan B
# F = [[2,4,6], [1,3,5]] # list genap dulu lalu ganjil, bukan range dari 0 sampai 20

# print(A)
# print(B)
# print(C)
# print(D)
# print(E)
# print(F)

# for i in range(10):
#    0, 1, 2, 3, dst
# increment
# auto increment

i = 0 # fungsi while perlu didefinisikan variabel yang digunakan

# while i < 10:
    #print("angka adalah : ", i) # while tidak auto increment sehingga "angka adalah 0" terus diprint tak terhingga

while i < 10:
    print("angka adalah : ", i) 
    # i = i + 1
    i += 1

print("=" * 100)

for i in range(10):
    print("angka adalah : ", i)

password = "rahasia"
cek = ''
# Dapat digunakan untuk pengecekan password ketika input password salah, program terus meminta masukan password hingga password benar
# Untuk menghentikan looping tak hingga, dapat ditekan ctrl+c
while cek != password:
    cek = input("Masukkan password : ")
    if cek != password:
        print("Password salah !")
    else:
        print("Password benar !")

password = "rahasia"
cek = ''
coba = 1
batascoba = 5
over = False
while cek != password : #and not over:
    if coba <= batascoba:
        cek = input("Masukkan password : ")
        if cek != password and coba < 5:
            coba += 1
            print("Password salah, silahkan coba lagi, percobaan ke - ", coba)
        elif cek != password and coba == 5:
            coba += 1
            print("Password salah, kesempatan habis, silakan menunggu beberapa jam untuk mencoba lagi")
        else:
            print("Password anda benar") # while akan terus looping selama cek tidak sama dengan password sehingga ketika password benar looping dihentikan
    #else:
        #over = True
        #print("Silakan menunggu beberapa jam untuk mencoba lagi")

### Team Assignment --- Present Jumat : Tim min 2 - 3 orang; kumpul paling lambat Kamis malam, present tiap tim hari Jumat
### CRUD = Create, Read, Update, Delete
# Membuat aplikasi mini (untuk data barang)
# ada menu :
# 1. Cetak isi daftar barang (Read)
# 2. Menambah Data ke daftar barang (Create)
# 3. Menghapus data dari daftar barang (Delete)
# 4. Mengubah data dalam daftar barang (Update)
# 5. Exit (keluar)

# Kondisi:
# 1. Read (Cetak data)
# Jika tidak ada data, keluar notif : Daftar Barang masih kosong
# Cetak seluruh isi daftar barang 
# 2. Create (Tambah Data)
# Pengecekan jenis data, notif : Data yang anda masukkan salah, misal: data yang dimasukkan hanya bisa string, tidak bisa angka
# Pengecekan duplikasi : keluar notif pilihan: Data sudah ada sebelumnya, apakah tetap akan disimpan? (Y/N)
# Y : keluar notif = Data Tersimpan
# N : keluar notif = Data Tidak Tersimpan
# Data langsung disimpan dan keluar notif : Data Tersimpan
# 3. Delete (Hapus Data)
# Jika data yang diminta user tidak ada, keluar notif: Nama Barang Tidak Ada
# Hapus seluruh data sesuai yang diminta user, contoh: Jika ada jeruk dalam daftar dan user memasukkan data jeruk, maka daftar jeruk ada 2. Bila daftar jeruk dihapus, semua daftar jeruk akan dihapus
# 4. Update (Ubah Data)
# Jika data yang diminta user tidak ada, keluar notif: Nama Barang Tidak Ada
# Update datanya contoh: jeruk -- ubah jadi jeruk bali
# Keluar notif Data Terupdate
# 5. Exit (Keluar Aplikasi)
# Selama user belum memilih opsi ini, Menu akan terus ditampilkan

### Personal Assignment
# Latihan 1:

# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

# Latihan 2:

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

# Latihan 3:

# 5
# 5 4
# 5 4 3
# 5 4 3 2
# 5 4 3 2 1

# Latihan 4:

# 1 1 1 1 1
# 2 2 2 2
# 3 3 3
# 4 4
# 5

# Latihan 5:
# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1

# Latihan 6:
# 5 4 3 2 1
# 5 4 3 2
# 5 4 3
# 5 4
# 5

# Latihan 7:
#         *
#       * * *
#     * * * * * 
#   * * * * * * *
# * * * * * * * * *
# * * * * * * * * *
#   * * * * * * *
#     * * * * *
#       * * * 
#         *
# Kirim email: khumaeni@purwadhika.com