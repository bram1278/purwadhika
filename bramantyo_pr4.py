# Latihan 1
# input : masukkan nama hari : SENIN atau selasA
# pengecekan input : "Tidak ada nama hari" lalu program di-close
#         jumlah : input hari yang diinginkan, cth: 100 hari atau -2 hari 
# output : (jumlah)hari dari sekarang adalah hari ....

try :
    hari = str(input("Masukkan nama hari: "))
    harilisthuruf = ["senin", "selasa", "rabu", "kamis", "jumat", "sabtu", "minggu"]

    jumlah =  int(input("Masukkan jeda hari (dalam angka dan boleh minus) yang ingin anda cari: "))

    harikecilhuruf = hari.lower()
 
    # menentukan nilai konstanta berdasarkan input "hari" yang dimasukkan
    if harikecilhuruf == harilisthuruf[0] :
        harikecilangka = 0
    elif harikecilhuruf == harilisthuruf[1] :
        harikecilangka = 1
    elif harikecilhuruf == harilisthuruf[2] :
        harikecilangka = 2
    elif harikecilhuruf == harilisthuruf[3] :
        harikecilangka = 3
    elif harikecilhuruf == harilisthuruf[4] :
        harikecilangka = 4
    elif harikecilhuruf == harilisthuruf[5] :
        harikecilangka = 5
    elif harikecilhuruf == harilisthuruf[6] :
        harikecilangka = 6
    
    hitung = harikecilangka + jumlah
    konstanta = 7
    # persamaan untuk menghitung hari apakah dari nilai variabel "jumlah" yang dimasukkan
    if hitung > 6 :
        hitung2 = hitung%konstanta    
    elif 0 <= hitung <= 6 :
        hitung2 = hitung
    elif -7 <= hitung <= -1 :
        hitung2 = konstanta + hitung
    elif hitung < -7 :
        if (-hitung)%konstanta == 0 :
            hitung2 = (-hitung)%konstanta
        else :
            hitungmin = - hitung
            hitungmin2 = hitungmin%konstanta
            hitung2 = konstanta - hitungmin2
    
    harihitung = harilisthuruf[hitung2]
    print(f"{jumlah} hari dari sekarang adalah hari {harihitung}")
except :
    print ("Nama hari atau jumlah hari yang anda masukkan salah")
    print ("Catatan: Gunakan kata 'jumat' atau 'Jumat', bukan 'jum'at' atau 'Jum'at'")

# Latihan 2
# palindrome; contoh kata katak kalau dibalik katak juga

# input : masukkan kata
# kondisi : dilakukan pengecekan kata
# output : kata tersebut termasuk/bukan palindrome

kata = str(input("Masukkan kata: "))
kataasli = list(kata) # list untuk kata yang diinput
kata2 = list(kata)
kata2.reverse() # list untuk kata yang dibalik
# mengecek apakah list dari kata asli dan kata yang dibalik adalah sama atau tidak
if kataasli == kata2 :
    print ("Kata tersebut termasuk palindrome")
else :
    print ("Kata tersebut tidak termasuk palindrome")

# Latihan 3
# masukkan kalimat : "hari ini hari selasa"
# ada 2 pilihan (opsi 1 dan opsi 2)
# opsi 1. masukkan karakter : "a"
# outputnya : hri ini hri sels (menghapus huruf "a")
# opsi 2. masukkan karakter vokal : "o"
# outputnya : horo ono horo soloso (semua huruf vokal diganti menjadi huruf "o")

kalimat = str(input("Masukkan kalimat: "))
kalimatkecil = kalimat.lower()
opsi = int(input("Masukkan opsi (dalam angka 1 atau 2) yang anda inginkan: "))

if opsi == 1 :
    kata1 = str(input("Masukkan huruf yang akan dihapus: "))
    katakecil1 = kata1.lower()
    kalimatkecil1 = kalimatkecil.replace(katakecil1,"") # menghapus kata yang dimasukkan dari kalimat yang diinput
    print(kalimatkecil1)

elif opsi == 2 :
    kata2 = str(input("Masukkan satu huruf vokal (a,i,u,e, atau o) yang diinginkan: "))
    katakecil2 = kata2.lower()
    if katakecil2 == "a" : # mengganti semua vokal jika input vokal adalah "a"
        kalimatkecil2a = kalimatkecil.replace("i",katakecil2)
        kalimatkecil2b = kalimatkecil2a.replace("u",katakecil2)
        kalimatkecil2c = kalimatkecil2b.replace("e",katakecil2)
        kalimatkecil2d = kalimatkecil2c.replace("o",katakecil2)
        print(kalimatkecil2d)
    elif katakecil2 == "i" : # mengganti semua vokal jika input vokal adalah "i"
        kalimatkecil2a = kalimatkecil.replace("a",katakecil2)
        kalimatkecil2b = kalimatkecil2a.replace("u",katakecil2)
        kalimatkecil2c = kalimatkecil2b.replace("e",katakecil2)
        kalimatkecil2d = kalimatkecil2c.replace("o",katakecil2)
        print(kalimatkecil2d)
    elif katakecil2 == "u" : # mengganti semua vokal jika input vokal adalah "u"
        kalimatkecil2a = kalimatkecil.replace("a",katakecil2)
        kalimatkecil2b = kalimatkecil2a.replace("i",katakecil2)
        kalimatkecil2c = kalimatkecil2b.replace("e",katakecil2)
        kalimatkecil2d = kalimatkecil2c.replace("o",katakecil2)
        print(kalimatkecil2d)
    elif katakecil2 == "e" : # mengganti semua vokal jika input vokal adalah "e"
        kalimatkecil2a = kalimatkecil.replace("a",katakecil2)
        kalimatkecil2b = kalimatkecil2a.replace("i",katakecil2)
        kalimatkecil2c = kalimatkecil2b.replace("u",katakecil2)
        kalimatkecil2d = kalimatkecil2c.replace("o",katakecil2)
        print(kalimatkecil2d)
    elif katakecil2 == "o" : # mengganti semua vokal jika input vokal adalah "o"
        kalimatkecil2a = kalimatkecil.replace("a",katakecil2)
        kalimatkecil2b = kalimatkecil2a.replace("i",katakecil2)
        kalimatkecil2c = kalimatkecil2b.replace("u",katakecil2)
        kalimatkecil2d = kalimatkecil2c.replace("e",katakecil2)
        print(kalimatkecil2d)
    else :
        print("Huruf yang anda masukkan bukan huruf vokal")
else :
    print("Opsi yang anda masukkan tidak terdaftar, masukkan angka 1 atau 2")

# Latihan 4
# (hanya menggunakan metode numerikal)
# Masukkan 4 digit angka : 5689 
# outputnya : 8956
# jika angka yang dimasukkan berupa string kata, keluar output : "Angka yang anda masukkan salah"

try:
    angka = int(input("Masukkan 4 digit angka: "))
except : 
    print ("Nilai yang anda masukkan salah")

else: 
    if 1000 <= angka < 10000 : # untuk memastikan angka yang dimasukkan adalah 4 digit
        x = angka%100 # dua digit puluhan dan satuan
        y = angka - x # dua digit ribuan dan ratusan
        x1 = x * 100 # dua digit ribuan dan ratusan yang baru
        y1 = y/100 # dua digit puluhan dan satuan yang baru
        totalbaru = int(x1 + y1) # untuk menghasilkan 4 digit yang baru
        print(totalbaru)
    else :
        print("Angka yang anda masukkan salah")

# Latihan 5
# (hanya menggunakan metode numerikal)
# input: masukkan angka 2 digit : 85
# masukkan 2 digit kedua : 32
# outputnya : 8532
# jika angka yang dimasukkan berupa string kata, keluar output : "Angka yang anda masukkan salah"

try:
    angka1 = int(input("Masukkan 2 digit angka pertama: "))
    angka2 = int(input("Masukkan 2 digit angka kedua: "))
except : 
    print ("Nilai yang anda masukkan salah")

else: 
    if 10 <= angka1 < 100 and 10 <= angka2 < 100 : # untuk memastikan angka yang dimasukkan adalah 4 digit
        x = angka1*100 # dua digit ribuan dan ratusan yang baru
        y = angka2 # dua digit puluhan dan satuan yang baru
        totalbaru = int(x + y) # untuk menghasilkan 4 digit yang baru
        print(totalbaru)
    else :
        print("Angka yang anda masukkan salah")