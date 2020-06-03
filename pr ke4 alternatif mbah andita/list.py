# Latihan conditional dan List: Andita

# input: masukkan nama hari dalam 1 minggu
# jumlah: 100 hari
# output: 100 hari dari {nama hari} adalah hari ...
# kondisi 2: tampilkan "Nama hari yang Anda masukkan salah", untuk tampilan error

# haridalamminggu = ['senin', 'selasa', 'rabu', 'kamis', 'jumat', 'sabtu', 'minggu']
# hari = input("Masukkan hari: ")

# harikecil = hari.lower()

# if harikecil not in haridalamminggu:
#     print("Hari yang Anda masukkan salah")
# else:
#     selisih = int(input("Masukkan selisih hari yang ingin ditentukan: "))
#     harikecil = hari.lower()
#     urutan = haridalamminggu.index(harikecil)
#     modulus = selisih % len(haridalamminggu)
#     dicari = urutan + modulus
#     # hari akan datang
#     indeksakandatang = dicari % len(haridalamminggu)
#     hariakandatang = haridalamminggu[indeksakandatang]
#     # hari yang lalu
#     selisihabs = abs(selisih)
#     indekslalu = urutan - selisihabs
#     harilalu = haridalamminggu[indekslalu]
#     if selisih > 0:
#         print(f"{selisih} hari setelah hari {hari.upper()} adalah hari {hariakandatang.upper()}")
#     else:
#         print(f"{selisihabs} hari sebelum hari {hari.upper()} adalah hari {harilalu.upper()}")


# lat 2
# palindrome
# katak - katak
# input: masukkan kata
# kondisi: dilakukan pengecekan kata
# output: kata tersebut termasuk/bukan palindrome

# kata = input("Masukkan kata: ")
# valuekata1 = list(kata)



# valuekata2 = valuekata1.copy()
# valuekata2.reverse()

# if (valuekata1) == (valuekata2):
#     print(f"kata {kata.upper()} adalah palindrome")
# else:
#     print(f"kata {kata.upper()} bukan palindrome")




# # latihan 3:
# masukkan kalimat: "Hari ini hari selasa"
# opsi 1:
# masukkan karakter: "a"
# outputnya: hri ini hri sels
# opsi 2:
# masukkan karakter vokal
# output: horo ono horo soloso

# kalimat = input("Masukkan kalimat: ")
# hapushuruf = input("Apakah Anda ingin menghapus karakter (Y/N)?  ")
# yeskecil = hapushuruf.lower()


# kalimatkecil = kalimat.lower()


# if yeskecil == 'y':
#     huruf = input("Karakter apa yang ingin dihapus? ")
#     hurufkecil = huruf.lower()
#     bagi = kalimatkecil.split(hurufkecil)
#     baru = ''.join(bagi)
#     print(f'''kalimat {kalimatkecil.upper()} yang dihapus karakter {hurufkecil.upper()}
#     menjadi: {baru}''')
# elif hapushuruf == 'n':
#     print("Karakter tidak dihapus")
# else:
#     print("Keterangan yang Anda masukkan salah")

# gantivokal = input("Apakah Anda ingin mengganti huruf vokal (Y/N)? ")
# konfirm = gantivokal.lower()

# if konfirm == 'y':
#     vokal = input("Masukkan karakter vokal yang akan diganti: ")
#     vokalkecil = vokal.lower()
#     gantia = kalimatkecil.replace('a', vokalkecil).replace('i', vokalkecil).replace('u', vokalkecil).replace('e', vokalkecil).replace('o', vokalkecil)
#     print(gantia)
# elif konfirm == 'n':
#     print("Huruf vokal tidak diganti")
# else:
#     print("Keterangan yang Anda masukkan salah")


# # lat 4
# (hanya menggunakan metode numerik)
# masukkan 4 digit angka: 5689
# output: 8956
# jika angka yang dimasukkan berupa string, keluar output: "Angka yang anda masukkan salah"

# try:
#     num = int(input("Masukkan 4 DIGIT angka: "))
#     ribuan = num // 1000
#     sisaribu = num % 1000
#     ratusan = sisaribu // 100
#     sisaratus = sisaribu % 100
#     puluhan = sisaratus // 10
#     satuan = sisaratus % 10
#     print(f"Hasil: {puluhan}{satuan}{ribuan}{ratusan}")
# except:
#     print("Angka yang Anda masukkan salah")

# # # lat 5
# # (hanya menggunakan metode numerik)
# # input: masukkan angka 2 digit: 85
# # masukkan 2 digit kedua: 32
# # outputnya: 8532
# # jika angka yang dimasukkan berupa string, keluar output: "Angka yang anda masukkan salah"

try:
    num1 = int(input("Masukkan 2 digit angka pertama: "))
    num2 = int(input("Masukkan 2 digit angka kedua: "))
    riburatus = num1 * 100
    lengkap = riburatus + num2
    print(f"Hasil: {lengkap}")
except:
    print("Angka yang Anda masukkan salah")
