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
