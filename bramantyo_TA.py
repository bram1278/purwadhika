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

def hurufkemorse(i): # input adalah len dari list 'hasil' yang berisi input user yang dipecah per alfabet atau angka
    for a in range(0,i):
        if hasil[a] in alnum:
            morse2 = lambda i, j, k, l: i[j.index(k[l])]            
            morse1[a] = morse2(morse,alnum,hasil,a)
    return morse1

def morsekehuruf(i): # input i adalah list yang isinya hasil pecahan kode morse
    alnum1 = i # alnum1 adalah variabel yang isi dan jumlah isinya bernilai sama dengan variabel cek
    for a in range(0,len(i)):
        if i[a] not in morse:
            print("Kode morse yang anda input salah atau tidak eksis")
            alnum1 = ['error']
            break
        else:
            alnum2 = lambda i, j, k, l: i[j.index(k[l])]  
            alnum1[a] = alnum2(alnum,morse,i,a)             
    return alnum1


if kecil.isalnum():
    a = hurufkemorse(x)
    print(f"Translasi dari kata {kecil} adalah {a}")
elif "." in kecil or "-" in kecil or "/" in kecil:
    cek = kecil.split("/")    
    if "" in cek: # mengecek apakah user menginput tanda / berturut-turut (cth: //, ///, dst)
        print("Input tidak bisa diproses karena anda memasukkan tanda / berturut-turut") # jika kondisi terpenuhi, notif error akan diprint    
    else :
        b = morsekehuruf(cek)
        print(f"Translasi dari kode {kecil} adalah {b}")    
else:
    print("Input yang anda masukkan salah (jangan ada spasi atau tanda / berturut-turut)")

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

romawi = list(daftar) # romawi adalah isi nilai key dari list kode yang mengandung nilai alfabet romawi (I, V, X, ...)
numeral = list(daftar.values()) # numeral adalah isi nilai values dari list kode yang mengandung nilai angka numeral (1, 5, 10, ...)

besar = angka.upper() # mengubah inputan "angka" dalam romawi menjadi huruf besar
besar1 = list(besar) # nilai "besar" diubah menjadi format list agar dapat dibandingkan dengan fungsi for dan if
batas = len(besar) # menghitung berapa banyak karakter romawi yang diinput user

romawi1 = [] # mengeset variabel romawi1 untuk digunakan pada fungsi roma(a) yang akan mengkonversi inputan angka numeral menjadi angka romawi
romawi2 = [] # mengeset variabel romawi1 untuk digunakan pada fungsi roma(a) yang akan mengkonversi inputan angka numeral menjadi angka romawi

for i in range(len(romawi)-1,-1, -1): 
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

    def numerik(b):        
        jumlah = 0 # mengeset local variable untuk menghitung jumlah total alfabet romawi yang diubah ke angka numeral
        jumlah1 = [] # mengeset local variabel "jumlah1" yang akan digunakan ketika mengecek apakah ada nilai minus yang dikenakan pada angka numeral yang telah dikonversi dari angka romawi
        cek = [] # mengeset  local variabel "cek" yang akan digunakan untuk menghitung dan membandingkan huruf romawi "besar1" terhadap urutan index dari list "romawi"  
        for a in range(0,b):
            if besar1[a] in romawi:                
                cek = romawi.index(besar1[a]) # menghitung huruf romawi besar1 yang sedang diperiksa saat ini dapat ditemukan pada list "romawi" pada index ke-berapa
                jumlah += numeral[cek] # nilai angka romawi yang dideteksi diubah setara dengan nilai index ke-"cek" yang ada di list "numeral"; ada error local variabel 'jumlah' referenced before assignment
                jumlah1.append(numeral[cek]) # variabel list jumlah1 menampung nilai hasil pengkonversian numeral[cek]
            else: # jika nilai list besar1[a] pada loop for ada yang mengandung nilai yang tidak terdaftar di list "romawi", notif error akan diprint 
                print("Huruf yang anda masukkan tidak termasuk angka romawi")
                break # loop for dihentikan
            if a > 0 and jumlah1[a] > jumlah1[a - 1]: # jika nilai numeral hasil konversi angka romawi yang didapat sekarang adalah lebih besar dari jumlah1 pada a sebelumnya, berarti nilai jumlah1[a - 1] bertanda minus
                jumlahminus = - (jumlah1[a - 1] * 2) # nilai jumlahminus adalah nilai jumlah1[a - 1] dikali dua karena variabel jumlah sudah menambahkan jumlahminus sebagai plus pada a sebelumnya
                jumlah = jumlah + jumlahminus
        return (jumlah)   

    num = numerik(batas)

    print(f"Hasil konversi angka romawi {angka} adalah {num}")

    
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

# translasi nama hari Inonesia - Inggirs atau sebaliknya 

daftarhari = {
    "senin" : "monday",
    "selasa" : "tuesday",
    "rabu" : "wednesday",
    "kamis" : "thursday",
    "jum'at" : "friday",
    "sabtu" : "saturday",
    "minggu" : "sunday",
}

hari = list(daftarhari)
day = list(daftarhari.values())

translasi = input("Masukkan input anda / Please insert your input : ") # translasi adalah variabel input nama hari yang dimasukkan user
translasi1 = translasi.lower()

if translasi1 in hari:        
    eng = lambda i, j, k: i[j.index(k)]  
    eng1 = eng(day,hari,translasi1) 
    print(f"Nama hari {translasi1} dalam bahasa Inggris adalah {eng1}")
elif translasi1 in day:
    indo = lambda i, j, k: i[j.index(k)]
    indo1 = indo(hari,day,translasi1) 
    print(f"Day {translasi1} in bahasa is {indo1}")
else:
    print("Input anda tidak terdeteksi / Your input is not detected \n Catatan: Gunakan hari jum'at atau Jum'at, bukan jumat atau Jumat")  