## Latihan

# Pakai def dengan return function
# Lat 1:
# Pakai def : 
# Kalkulator (+,-, /, *)

# inputan:
# input angka 1 : 8
# input angka 1 : 10
# masukkan operator : +


angka1 = float(input('Silahkan masukkan angka 1: ')) # user memasukkan input angka1 dalam float agar bisa operasi angka desimal
angka2 = float(input('Silahkan masukkan angka 2: ')) # user memasukkan input angka1 dalam float agar bisa operasi angka desimal
operator = input('Silahkan masukkan operator (tambah, kurang, kali, bagi) : ') # user memasukkan input angka2
kecil = operator.lower() # input operator dibuat menjadi tanda kecil agar tidak case sensitive

def tambah(angka1,angka2): # tambah digunakan karena simbol + tidak bisa digunakan sebagai funngsi
    return angka1 + angka2       

def kurang(angka1,angka2): 
    return angka1 - angka2   
    
def kali(angka1,angka2): 
    return angka1 * angka2       

def bagi(angka1,angka2): # tambah digunakan karena simbol + tidak bisa digunakan sebagai funngsi
    return angka1 / angka2       

if kecil == 'tambah':    
    jumlah = round(tambah(angka1,angka2), 2) # untuk membulatkan hasil sebesar 2 angka di belakang koma
    print(f"Hasil penjumlahan {angka1} + {angka2} = ", jumlah)
elif kecil == 'kurang':        
    jumlah = round(kurang(angka1,angka2), 2)
    print(f"Hasil pengurangan {angka1} - {angka2} = ", jumlah)
elif kecil == 'kali':    
    jumlah = round(kali(angka1,angka2), 2)
    print(f"Hasil perkalian {angka1} * {angka2} = ", jumlah)
elif kecil == 'bagi':    
    jumlah = round(bagi(angka1,angka2), 2)
    print(f"Hasil perkalian {angka1} / {angka2} = ", jumlah)
else: 
    print('Inputan yang anda masukkan salah')


# Lat 2:
# pakai dict dan def:
# kamus = IND - ENG untuk hari 

# Translator (Encoder-Decoder Kode Morse)
# Silakan masukkan kalimat : Aman
# Output nya: (kode morse nya) .- / - - / .-/ -.

# Silakan masukkan kalimat: .- / - - / .-/ -.
# Output nya: Aman
# Tidak ada pilihan apakah ingin translasi Indo ke morse atau morse ke Indo

kode = {"a" : ".-", "b" : "-...", "c" : "-.-.", "d" : "-..", "e" : ".", "f" : "..-.", "g" : "--.", "h" : "....", "i" : "..", "j" : ".---", "k" : "-.-", "l" : ".-..", "m" : "--",
         "n" : "-.", "o" : "---", "p" : ".--.", "q" : "--.-", "r" : ".-.", "s" : "...", "t" : "-", "u" : "..-", "v" : "...-", "w" : ".--", "x" : "-..-", "y" : "-.--", "z" : "--..",
         "0" : "-----", "1" : ".----", "2" : "..---", "3" : "...--", "4" : "....-", "5" : ".....", "6" : "-....", "7" : "--...", "8" : "---..", "9" : "----." }

kalimat = input('Silahkan masukkan kata (jangan input spasi) atau kode morse anda (gunakan tanda / untuk pemisah antar kode morse): ')
kecil = kalimat.lower()

alnum = list(kode) # alnum adalah isi nilai key dari list kode yang mengandung nilai alfabet atau angka
morse = list(kode.values()) # morse adalah isi nilai values dari list kode yang mengandung nilai titik (.) atau strip (-)

hasil = list(kecil) # kata-kata yang telah displit spasi dimasukkan ke dalam sebuah list (set tidak dipakai karena akan mengeliminasi kata duplikat)
x = len(hasil)

morse1 = hasil # morse1 adalah variabel yang isi dan jumlah isinya bernilai sama dengan hasil

def hurufkemorse(i):
    for a in range(0,i):
        if hasil[a] in alnum:
            morse1[a] = morse[alnum.index(hasil[a])] # jika perintah ini dijalankan saat morse1 diset [], akan didapat pesan "index out of range"
    return morse1

if kecil.isalnum():
    a = hurufkemorse(x)
    print(f"Translasi dari kata {kecil} adalah {a}")
elif "." in kecil or "-" in kecil or "/" in kecil:
    cek = kecil.split("/")
    alnum1 = cek # alnum1 adalah variabel yang isi dan jumlah isinya bernilai sama dengan variabel cek
    if "" in cek: # mengecek apakah user menginput tanda / berturut-turut (cth: //, ///, dst)
        print("Input tidak bisa diproses karena anda memasukkan tanda / berturut-turut") # jika kondisi terpenuhi, notif error akan diprint
    for a in range(0,len(cek)):
        if cek[a] not in morse:
            print("Kode morse yang anda input salah atau tidak eksis")
            break
        else: 
            alnum1[a] = alnum[morse.index(cek[a])] # jika perintah ini dijalankan saat alnum1 diset [], akan didapat pesan "index out of range"
    print(f"Translasi dari kode {kecil} adalah {alnum1}")
    
else:
    print("Input yang anda masukkan salah")

# Lat 3:
# Pakai def
# Fizz Buzz
# input masukkan angka :
# outputnya : 
# angka yang habis dibagi 3 : Fizz
# angka yang habis dibagi 5 : Buzz
# angka yang habis dibagi 3 dan 5: Fizz Buzz
# cth output: 1
# 2
# Fizz
# 4
# Buzz
# Fizz
# 7
# 8
# Fizz
# Buzz

angka = int(input('Silahkan masukkan angka: '))

def FB(x):
    if x%3 == 0 and x%5 == 0:
        return("Fizz Buzz")
    elif x%3 == 0:
        return("Fizz")
    elif x%5 == 0:
        return("Buzz")
    else:
        return(x)

print(FB(angka))

# Lat 4: 
# pakai def: 
# Caesar cipher
# masukkan kata : Joni
# masukkan angka : 2
# hasil caesar cipher : Lnpk (huruf maju dua)

# masukkan kata : Joni
# masukkan angka : -2
# hasil caesar cipher : hmlg  (huruf mundur dua)

alfabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] # list berisi urutan alfabet

kata = input('Silahkan masukkan kata (jangan masukkan angka, spasi, atau tanda simbol lainnya): ')
angka = int(input('Silahkan masukkan angka (bisa bertanda plus atau minus): '))

kecil = kata.lower() # agar input user tidak case sensitive
katabaru = ''

batas = len(alfabet) # bernilai 26, konstanta bertipe int yang menjadi penentu kondisi if agar operasi pergeseran alfabet tidak keluar dari rentang index yang diizinkan

if kecil.isalpha() : # mengecek apakah input user adalah alfabet saja (True) atau tidak (False)
    cek = list(kecil) # mengubah input kata menjadi list yang isinya masing-masing alfabet
    for a in range(0,len(cek)):
        cek1 = alfabet.index(cek[a]) # perintah index untuk mengecek urutan ke-berapakah input user pada daftar alfabet; tidak bisa dijalankan untuk objek set sehingga digunakan list 
        if cek1 + angka <= (batas - 1):
            katabaru = katabaru + alfabet[cek1 + angka] # katabaru adalah kata dari alfabet yang urutannya telah dijumlahkan/dikurangi dengan input angka, cek1 bertipe int
        elif cek1 + angka > (batas - 1): # jika hasil penjumlahan cek1 dan angka di atas alfabet ke-26 (z), cth: z dinaikkan sebesar 1 akan berubah menjadi a
            katabaru = katabaru + alfabet[cek1 + angka%26 - (batas)]
        elif cek1 + angka < 0: # jika hasil pengurangan cek1 dan angka di bawah alfabet pertama (a), cth: a diturunkan sebesar 1 akan berubah menjadi z
            katabaru = katabaru + alfabet[cek1 + angka%26 + (batas)]
    print(f"Kata yang baru menjadi ",katabaru)
else: 
    print("Inputan anda salah")

# Latihan 5
# pakai def dan dict
# Batas maksimal 4000
# keluar notif: angka di luar jangkauan
# Translator (Encoder-Decoder Angka Romawi)
# Silakan masukkan angka : 2018
# Output nya: (angka romawinya) MMXVIII

# Silakan masukkan kalimat: MMXVIII
# Output nya: 2018
# Tidak ada pilihan apakah ingin translasi nomor ke romawi atau romawi ke nomor

# Catatan: I = 1, V = 5, X = 10, L = 50, C = 100, D = 500, M = 1000

# Kirim Email

daftar = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000}
angka = input('Silahkan masukkan angka numerik atau romawi yang positif dan kurang dari 4000: ')

romawi = list(daftar) # alnum adalah isi nilai key dari list kode yang mengandung nilai alfabet atau angka
numeral = list(daftar.values()) # morse adalah isi nilai values dari list kode yang mengandung nilai titik (.) atau strip (-)

jumlah = 0 # mengeset variabel "jumlah" yang akan digunakan ketika mengkonversi angka romawi menjadi angka numeral
jumlah1 = [] # mengeset variabel "jumlah1" yang akan digunakan ketika mengecek apakah ada nilai minus yang dikenakan pada angka numeral yang telah dikonversi dari angka romawi

besar = angka.upper() # mengubah inputan "angka" dalam romawi menjadi huruf besar
besar1 = list(besar) # nilai "besar" diubah menjadi format list agar dapat dibandingkan dengan fungsi for dan if
batas = len(besar) # menghitung berapa banyak karakter romawi yang diinput user

romawi1 = [] # mengeset variabel romawi1 untuk digunakan pada fungsi roma(a) yang akan mengkonversi inputan angka numeral menjadi angka romawi
romawi2 = [] # mengeset variabel romawi1 untuk digunakan pada fungsi roma(a) yang akan mengkonversi inputan angka numeral menjadi angka romawi

for i in range(6,-1, -1): 
    if (i%2 == 0):
        romawi1.append(romawi[i]) # mengeset romawi1 = ['M', 'C', 'X', 'I']
    elif (i%2 == 1):
        romawi2.append(romawi[i]) # mengeset romawi2 = ['D', 'L', 'V']


def digit(a):
    a1 = int(a)
    x = a1%100 # dua digit puluhan dan satuan
    y = a1 - x # dua digit ribuan dan ratusan
    satuan = x%10 # mendapatkan nilai satuan
    x1 = x - satuan # mendapatkan nilai puluhan (masih berakhiran 0, cth: 10, 20, 30, dst)
    puluhan = int(x1 / 10) # mendapatkan nilai puluhan; int digunakan untuk mengkonversi tipe data dari float menjadi int       
    y1 = y%1000 # mendapatkan nilai ratusan (masih berakhiran 00, cth: 100, 200, 300, dst)
    ratusan = int(y1/100) # mendapatkan nilai ratusan; int digunakan untuk mengkonversi tipe data dari float menjadi int   
    y2 = y - y1 # mendapatkan nilai ribuan (masih berakhiran 000, cth: 1000, 2000, 3000, dst)
    ribuan = int(y2/1000) # mendapatkan nilai ribuan; int digunakan untuk mengkonversi tipe data dari float menjadi int   
    return (ribuan, ratusan, puluhan, satuan)
    
def roma(a): # fungsi untuk mengubah angka numeral menjadi angka romawi
    x = len(a)
    r = ''
    for i in range(0,x): # fungsi for untuk mengecek nilai a[i]
        if a[i] == 0:
            r = r + ''            
        if 1 <= a[i] <= 3:
            r = r + romawi1[i]*a[i]
        elif a[i] == 4:
            r = r + romawi1[i] + romawi2[i-1]
        elif a[i] == 5:
            r = r + romawi2[i-1]
        elif 6 <= a[i] <= 8:
            r = r + romawi2[i-1] + romawi1[i]*((a[i]%3)+1)
        elif a[i] == 9:
            r = r + romawi1[i] + romawi1[i-1] 
    return (r)

if angka.isalpha() : # mengecek apakah input user adalah alfabet saja (True) atau tidak (False)
    besar = angka.upper() # mengubah inputan "angka" dalam romawi menjadi huruf besar
    besar1 = list(besar) # nilai "besar" diubah menjadi format list agar dapat dibandingkan dengan fungsi for dan if
    batas = len(besar) # menghitung berapa banyak karakter romawi yang diinput user
    
    for a in range(0,batas):
        if besar1[a] in romawi:
            cek = romawi.index(besar1[a]) # menghitung huruf romawi besar1 yang sedang diperiksa saat ini dapat ditemukan pada list "romawi" pada index ke-berapa
            jumlah += numeral[cek] # nilai angka romawi yang dideteksi diubah setara dengan nilai index ke-"cek" yang ada di list "numeral"
            jumlah1.append(numeral[cek]) # variabel list jumlah1 menampung nilai hasil pengkonversian numeral[cek]
            if a > 0 and jumlah1[a] > jumlah1[a - 1]: # jika nilai numeral hasil konversi angka romawi yang didapat sekarang adalah lebih besar dari jumlah1 pada a sebelumnya, berarti nilai jumlah1[a - 1] bertanda minus
                jumlahminus = - (jumlah1[a - 1] * 2) # nilai jumlahminus adalah nilai jumlah1[a - 1] dikali dua karena variabel jumlah sudah menambahkan jumlahminus sebagai plus pada a sebelumnya
                jumlah = jumlah + jumlahminus
        elif besar1[a] not in romawi: # jika nilai list besar1[a] pada loop for ada yang mengandung nilai yang tidak terdaftar di list "romawi", notif error akan diprint 
            print("Huruf yang anda masukkan tidak termasuk angka romawi")
            break # loop for dihentikan
            
    print(f"Hasil konversi angka romawi {angka} adalah {jumlah}")

    
elif angka.isnumeric() :
    angka1 = int(angka)
    if angka1 >= 4000 or angka1 <= 0:
        print("rentang nomor yang anda masukan tidak terdeteksi")
    else:
        x = digit(angka1) # fungsi untuk mendapatkan nilai ribuan, ratusan, puluhan, dan satuan secara berurutan dalam bentuk list        
        rom = roma(x) # fungsi untuk mendapatkan konversi huruf romawi dari input angka numeral yang dimasukkan user        
        print(f"Hasil konversi angka numeral {angka} adalah {rom}")
else:
    print('Inputan anda tidak terdeteksi')

## Lat 6 
# Pakai def function
# konversi angka digital
# Masukkan angka : 9
# outputnya
#  __
# |__|
#  __|

## Rekursive Function # ada function di dalam function tetapi berulang-ulang