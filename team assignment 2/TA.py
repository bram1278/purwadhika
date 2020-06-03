
ID = ['']
passWORD = ['']
e_mail = ['']
Nama = ['']
Gender = ['']
Usia = ['']
Job = ['']
Hobby = ['']
Alamat = ['']
NamaKota = ['']
RT = ['']
RW = ['']
ZipCode = ['']
Lat = ['']
Lang = ['']
HP = ['']

loop = True
while loop:
    print('===== MENU =====')
    print('[1] LOGIN\n[2] REGISTER')
    pilihan = input('masukkan pilihan [1/2]:')
    if pilihan == '1':
        print('=== LOGIN ===')
        userID = input('User ID:')
        password = input('Password:')
        i = len(ID)
        for n in range(0,i):
            if userID not in ID: 
                print('\n"Anda belum register atau ID / Password anda salah"\n')
                break
            elif userID == ID[n]:
                cari_index_userID = ID.index(userID)
                cari_index_password = passWORD.index(password)
                if cari_index_userID == cari_index_password:
                    print('\n"Anda berhasil login"\n')
                    loop = False

    elif pilihan == '2':
        print('=== REGISTER ===')
        reg = True
        while reg:
            userID = input('User ID: ')
            if userID.isdigit():
                print('user ID yang anda masukkan salah \nUser ID harus meliputi huruf dan angka \n')
            elif userID.isalpha():
                print('user ID yang anda masukkan salah \nUser ID harus meliputi huruf dan angka \n')
            elif userID in ID:
                print("User ID telah digunakan")
            elif userID.isalnum():
                reg = False
            else:
                print('user ID yang anda masukkan salah \nUser ID harus meliputi huruf dan angka \n')
        ID.append(userID)
        pword = True
        while pword:
            password = input('password: ')
            if (len(password) < 8):
                print('Password salah! \nPassword harus gabungan huruf kapital, huruf kecil dan angka, minimal 8 karakter')
            elif password.isdigit():
                print('Password salah! \nPassword harus gabungan huruf kapital, huruf kecil dan angka, minimal 8 karakter')
            elif password.isalpha():
                print('Password salah! \nPassword harus gabungan huruf kapital, huruf kecil dan angka, minimal 8 karakter')
            elif password.isupper():
                print('Password salah! \nPassword harus gabungan huruf kapital, huruf kecil dan angka, minimal 8 karakter')
            elif password.islower():
                print('Password salah! \nPassword harus gabungan huruf kapital, huruf kecil dan angka, minimal 8 karakter')
            elif password.isalnum():
                pword = False
            else :
                print('Password salah! \nPassword harus gabungan huruf kapital, huruf kecil dan angka, minimal 8 karakter')
        passWORD.append(password)
        EMail = True
        while EMail:
            email = input('Alamat Email:')
            a = email.split('@')
            namauser = a[0]
            hosting = a[1].split('.')[0]
            ekstensi = a[1].split('.')[-1]
            salah = 0
            for i in range(0,len(namauser)):
                if not ((namauser[i] >= '1' and namauser[i] <= '9') or (namauser[i] >= 'a' and namauser[i] <= 'z') or (namauser[i] >= 'A' and namauser[i] <= 'Z') or namauser[i] == '.' or namauser[i] == '_') or len(a)>2:
                    salah += 1
                    print('Format username dari email yang anda masukkan salah')
                    break
            for i in range(0, len(hosting)):
                if not (hosting[i].isalpha() or hosting[i].isdigit()):
                    salah += 1
                    print('Format hosting dari email yang anda masukkan salah')
                    break
            for i in range(0,len(ekstensi)):
                if '' in a[-1].split('.'):
                    salah += 1
                    print('Format ekstensi dari email yang anda masukkan salah')
                    break
                if not (ekstensi[i].isalpha() and len(a[-1].split('.')) <= 3 and len(ekstensi)<= 5):
                    salah += 1
                    print('Format ekstensi dari email yang anda masukkan salah')
                    break
            if salah == 0:
                EMail = False
        e_mail.append(email)
        print('\n"Anda berhasil Register"\n')
        print('Mohon isi biodata dibawah ini')
        nama = input('Nama:').title()
        gender = input('Gender:').title()
        usia = input('Usia (tahun):').title()
        job = input('Pekerjaan:').title()
        hobby = input('Hobby (boleh lebih dari satu):').title()
        alamat = input('Alamat:').title()
        namakota = input('Nama Kota:').title()
        rt = input('RT:')
        rw = input('RW:')
        zip = input('Zip Code:')
        lat = input('-Geo- \nLat:')
        lang = input('Lang:')
        hp = input('No HP: ')
        simpan = True
        while simpan:
            Simpan = input(' \nApakah anda ingin menyimpan data? [Y/N]:').lower()
            if Simpan == 'y':
                Nama.append(nama)
                Gender.append(gender)
                Usia.append(usia)
                Job.append(job)
                Hobby.append(hobby)
                Alamat.append(alamat)
                NamaKota.append(namakota)
                RT.append(rt)
                RW.append(rw)
                ZipCode.append(zip)
                Lat.append(lat)
                Lang.append(lang)
                HP.append(hp)
                print('Data telah tersimpan')
                simpan = False
            elif Simpan == 'n':
                print('Data tidak tersimpan')
                simpan = False
            else:
                print('Pilihan yang anda masukkan salah')
        print('\n "Terima kasih" \n')
    else:
        print('pilihan yang anda masukkan salah')

def jumlah(angka1,angka2):
    jumlah = angka1 + angka2
    print(f'hasil penjumlahan {angka1} + {angka2} = {jumlah}')

def kurang(angka1,angka2):
    kurang = angka1 - angka2
    print(f'hasil pengurangan {angka1} - {angka2} = {kurang}')

def kali(angka1,angka2):
    kali = angka1 * angka2
    print(f'hasil perkalian {angka1} * {angka2} = {kali}')

def bagi(angka1,angka2):
    bagi = angka1 / angka2
    print(f'hasil pembagian {angka1} / {angka2} = {bagi}')

def akar(angka1):
    import math
    akar = math.sqrt(angka1)
    print(f'hasil akar dari {angka1} adalah {akar}')

def kuadrat(angka1):
    kuadrat = angka1 ** 2
    print(f'hasil kuadrat dari {angka1} adalah {kuadrat}')

def kubik(angka1):
    kubik = angka1 ** 3
    print(f'hasil kubik dari {angka1} adalah {kubik}')

def menghapus (Kalimat):
    Huruf = input('masukkan huruf yang akan dihilangkan:');
    print('hasil setelah dihilangkan:', Kalimat.replace(Huruf,''))
        
def mengganti (Kalimat):
    Huruf_vokal = input('masukkan karakter vokal:')
    hasil = Kalimat.replace('a',Huruf_vokal)
    hasil1 = hasil.replace('i',Huruf_vokal)
    hasil2 = hasil1.replace('u',Huruf_vokal)
    hasil3 = hasil2.replace('e',Huruf_vokal)
    hasil4 = hasil3.replace('o',Huruf_vokal)
    print('hasil setelah diganti:', hasil4)

def balikkata (Kalimat):
    kal1 = Kalimat.split()
    x = ''
    for i in kal1:
        j = i[::-1]
        x += j + ' '
    print(f'hasil pembalikkan kata dari kalimat "{Kalimat}" adalah "{x}"')


print('=+=+=+=+= SELAMAT DATANG =+=+=+=+=')

cek = 13
opsiuser = 1

while cek != opsiuser:
    print('\n===== MENU UTAMA =====')
    print('[1] DATA USER')
    print('[2] KONVERSI MORSE')
    print('[3] KALKULATOR SEDERHANA')
    print('[4] KONVERSI ROMAWI')
    print('[5] MENGHITUNG HARI')
    print('[6] TRANSLATE HARI')
    print('[7] MANIPULASI KARAKTER')
    print('[8] KONVERSI JUMLAH HARI')
    print('[9] NILAI FAKTORIAL')
    print('[10] JUMLAH ANGKA FIBONACCI')
    print('[11] MELIHAT SELURUH USER ID, PASSWORD, DAN EMAIL DATABASE')
    print('[12] MENU CRUD')
    print('[13] KELUAR')

    print('\n=====PILIHAN=====')
    opsi = input('Masukan pilihan dari 1 sampai 13: ')

    if opsi == '1':
        print('\n=== DATA USER ===')
        user_ID = input('Masukkan User ID Anda: ')
        if user_ID in ID: 
            i = ID.index(user_ID)
            print(f'Nama: {Nama[i]} \nGender: {Gender[i]} \nUsia: {Usia[i]} \nAlamat Email: {e_mail[i]} \nPekerjaan: {Job[i]} \nHobby: {Hobby[i]} \nAlamat: {Alamat[i]} \nKota: {NamaKota[i]} \nRT: {RT[i]} \nRW: {RW[i]} \nZip Code: {ZipCode[i]} \nGeo: \nLat: {Lat[i]} Lang: {Lang[i]} \nNo HP: {HP[i]}')
            break
        else:
            print('Data yang anda masukkan salah!')



    elif opsi == '2':
        print('\n=== KONVERSI MORSE ===')
        kode = {"a" : ".-", "b" : "-...", "c" : "-.-.", "d" : "-..", "e" : ".", "f" : "..-.", "g" : "--.", "h" : "....", "i" : "..", "j" : ".---", "k" : "-.-", "l" : ".-..", "m" : "--",
         "n" : "-.", "o" : "---", "p" : ".--.", "q" : "--.-", "r" : ".-.", "s" : "...", "t" : "-", "u" : "..-", "v" : "...-", "w" : ".--", "x" : "-..-", "y" : "-.--", "z" : "--..",
         "0" : "-----", "1" : ".----", "2" : "..---", "3" : "...--", "4" : "....-", "5" : ".....", "6" : "-....", "7" : "--...", "8" : "---..", "9" : "----." }
        opsi2 = True
        while opsi2:
            pilih2 = input('Masukkan "kata" atau "kembali" ke menu utama:').lower()
            if pilih2 == "kata":
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
            elif pilih2 == 'kembali':
                opsi2 = False
            else:
                print('Pilihan hanya "kata" atau "kembali"')



    elif opsi == '3':
        opsi3 = True
        while opsi3:
            print('\n===== KALKUATOR SEDERHANA =====')
            print('[1] Penjumlahan \n[2] Pengurangan \n[3] Perkalian \n[4] Pembagian \n[5] Akar \n[6] Pangkat 2 / Kuadrat \n[7] Pangkat 3 / Kubik \n[0] Pilihan Menu Utama')
            operator = input('masukkan pilihan operator [1-7]:')
            if operator == '1':
                print('=== PENJUMLAHAN ===')
                jumlah(int(input('Angka 1:')), int(input('Angka 2:')))
            elif operator == '2':
                print('=== PENGURANGAN ===')
                kurang(int(input('Angka 1:')), int(input('Angka 2:')))
            elif operator == '3':
                print('=== PERKALIAN ===')
                kali(int(input('Angka 1:')), int(input('Angka 2:')))
            elif operator == '4':
                print('=== PEMBAGIAN ===')
                bagi(int(input('Angka 1:')), int(input('Angka 2:')))
            elif operator == '5':
                print('=== AKAR ===')
                akar(int(input('Angka:')))
            elif operator == '6':
                print('=== PANGKAT 2 / KUADRAT ===')
                kuadrat(int(input('Angka:')))
            elif operator == '7':
                print('=== PANGKAT 3 / KUBIK ===')
                kubik(int(input('Angka:')))
            elif operator == '0':
                opsi3 = False
            else:
                print('Pilihan yang anda masukkan salah!')



    elif opsi == '4':
        print('\n=== KONVERSI ROMAWI ===')
        opsi4 = True
        pilih4 = input('Masukkan kata "angka" atau "kembali" untuk ke menu awal: ').lower()
        if pilih4 == 'angka':
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
        elif pilih4 == 'kembali':
            opsi4 = False
        else:
            print('Pilihan hanya "kata" atau "kembali"')



    elif opsi == '5':
        print('\n=== MENGHITUNG HARI ===')
        hari = ['senin', 'selasa', 'rabu', 'kamis', 'jumat', 'sabtu', 'minggu']
        hari1 = input('masukkan nama hari:').lower()
        jumlah_hari = int(input('masukkan jumlah hari:'))
        var1 = jumlah_hari%7
        var2 = hari.index(hari1)
        var3 = (var1+var2)%7
        var4 = hari[var3]
        print(f'hari ke',jumlah_hari, 'dari hari', hari1, 'adalah hari', var4)



    elif opsi == '6':
        print('\n=== TRANSLATE HARI ===')
        opsi6 = True
        while opsi6:
            print('[1] Masukkan nama hari / Input the name of the day \n[0] Kembali ke Menu Utama / Back to Menu')
            pilih6 = input('[1/0]: ')
            if pilih6 == '1':
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
                    print(f"Nama hari {translasi1} dalam bahasa Inggris adalah {eng1} \n")
                elif translasi1 in day:
                    indo = lambda i, j, k: i[j.index(k)]
                    indo1 = indo(hari,day,translasi1) 
                    print(f"Day {translasi1} in bahasa is {indo1} \n")
                else:
                    print("Input anda tidak terdeteksi / Your input is not detected \n Catatan: Gunakan hari jum'at atau Jum'at, bukan jumat atau Jumat")
            elif pilih6 == '0':
                opsi6 = False
            else:
                print('Pilihan yang anda masukkan salah! Your input is wrong!')



    elif opsi == '7':
        opsi7 = True
        while opsi7:
            print('\n=== MANIPULASI KARAKTER ===')
            print('[1] Menghapus karakter / huruf \n[2] Mengganti huruf vocal \n[3] Membalikkan kata tiap kalimat \n[0] Pilihan Menu Utama')
            pilih = input('pilihan [1/2/3/0]: ')
            if pilih == "1":
                menghapus(input("Masukkan Kalimat: "))
            elif pilih == "2":
                mengganti(input("Masukkan Kalimat: "))
            elif pilih == '3':
                balikkata(input("Masukkan Kalimat: "))
            elif pilih == '0':
                opsi7 = False
            else:
                print('Pilihan yang anda masukkan salah!')



    elif opsi == '8':
        print('\n=== KONVERSI JUMLAH HARI ===')
        days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

        userinputdays = str(input("what day is today? ")).lower()

        if (userinputdays == "monday"):
            convert = 0
        elif (userinputdays == "tuesday"):
            convert = 1
        elif (userinputdays == "wednesday"):
            convert = 2
        elif (userinputdays == "thursday"):
            convert = 3
        elif (userinputdays == "friday"):
            convert = 4
        elif (userinputdays == "saturday"):
            convert = 5
        elif (userinputdays == "sunday"):
            convert = 6
        else:
            print("please enter the correct day")
            
        userinputduration = int(input("how many days to fast forward? "))
        converteddays = (days[(convert+userinputduration) % 7])

        import math

        tahun = math.floor(userinputduration/360)
        leftoveryear = userinputduration % 360
        bulan = math.floor(leftoveryear / 30)
        leftovermonth = leftoveryear % 30
        minggu = math.floor(leftovermonth / 7)

        print (userinputduration , "days consists of, " , tahun, "years" , bulan , "months" , minggu , "weeks")
        print('and ',userinputdays,'forward will be on' , converteddays)


    elif opsi == '9':
        print('\n=== NILAI FAKTORIAL ===')
        faktorial = 1
        factorialinput = int(input('Masukkan angka yang akan difaktorialkan: '))
        if factorialinput <= 0:
            print('Mohon masukkan angka yang lebih besar')
        else:
            for i in range(1,factorialinput+1):
                faktorial = faktorial*i
            print(f'Hasil faktorial dari {factorialinput} adalah {faktorial}')



    elif opsi == '10':
        print('\n=== JUMLAH ANGKA FIBONACCI ===')
        opsi10 = True
        while opsi10:
            print('[1] Angka Fibonacci \n[0] Kembali ke Menu Utama')
            pilih10 = input('[1/0]: ')
            if pilih10 == '1':
                def fibnum(x):
                    if x <= 1:
                        return x
                    else:
                        return (fibnum(x-1) + fibnum(x-2))

                inputuser = int(input('Silakan masukkan nomor yang ingin dikonversi menjadi urutan Fibonacci: '))

                if inputuser <= 0:
                    print ('Mohon masukkan angka yang lebih besar')
                else:
                    print('\n')
                    print(f'Urutan Fibonacci',inputuser, 'adalah')
                    for i in range(0,inputuser):
                        print(fibnum(i),end = ',')
            elif pilih10 == '2':
                opsi10 = False
            else:
                print('Pilihan yang anda masukkan salah!')



    elif opsi == '11':
        print('\n=== MELIHAT SELURUH DATABASE ===')
        print('User ID: ', ID)
        print('Password: ', passWORD)
        print('Email: ', e_mail)



    elif opsi == '12':
        print('\n=== CRUD ===')
        opsi12 = True
        while opsi12:
            print('\n### MENU LOG ###')
            print('[1] SHOW LOG \n[2] CREATE LOG \n[3] REMOVE LOG \n[4] UPDATE LOG \n[5] BACK TO MAIN MENU')
            fruits = ['apple','banana','pear','cherry','kiwi','oranges']
            vegetables = ['cucumber','kale','cauliflower','broccoli','spinach']
            instants = ['corned beef','instant noodle','chicken nugget','canned sardines','spam']
            opsiuser = (input('please press [1/2/3/4/5]: '))
            if opsiuser == '1':
                print('=== SHOW LOG ===')
                print('fruits: ',fruits) 
                if fruits == []: # jika isi list dari fruits kosong
                    print('The fruits list is empty') 
                print('vegetables: ', vegetables) 
                if vegetables == []: # jika isi list dari vegetables kosong 
                    print('The vegetables list is empty')
                print('instants:', instants)
                if instants == []: # jika isi list dari instants kosong 
                    print('The instants list is empty')

            elif opsiuser == '2': # jika user memilih opsi untuk menambahkan data baru ke sebuah list
                print('=== CREATE LOG ===')
                var = input('fruits/vegetables/instants:') # user memilih input list mana yang akan ditambahkan data baru
                if var == 'fruits':
                    edit = input('please input item that you want to add:') # mengeset variabel input bernama edit
                    editx = edit.lower() # variabel input edit yang di-lowercase
                    i = len(fruits) # menghitung berapa banyak isi list fruits
                    for n in range(0,i+1): # mengeset looping for dengan variabel n sebagai variabel penentu dan batasnya ditentukan variabel i
                        if n == i: # jika n telah bernilai sama dengan i
                            fruits.append(editx) # variabel editx (input user yang di-lowercase) ditambahkan ke list yang ditangani pada pengulangan ini
                            print('The data that you input is saved') # memprint tanda notif bahwa input user berhasil ditambahkan ke list
                            print('fruits:',fruits) # memprint list yang baru
                            break # mengakhi for looping
                        elif editx == fruits[n]: # jika editx bernilai sama dengan isi index dari list yang dicari pada pengulangan ini
                            create = str(input('The list already contained the data that you input, do you want to add it? (Y/N)')) # buat variabel input create yang menentukan apakah user tetap ingin menambahkan atau tidak
                            create2 = create.lower() # variabel input create yang di-lowercase bernama create2
                            if create2 == 'y': # jika user menginput 'y' atau 'Y'
                                fruits.append(editx) # variabel editx (input user yang di-lowercase) ditambahkan ke list yang ditangani pada pengulangan ini
                                print('The data that you input is saved') # memprint tanda notif bahwa input user berhasil ditambahkan ke list
                                print('fruits:',fruits) # memprint list yang baru
                                break # mengakhiri for looping
                            elif create2 == 'n': # jika user menginput 'n' atau 'N'
                                print('The data that you input is not saved') # memprint tanda notif bahwa input user tidak ditambahkan ke list
                                print('fruits:',fruits) # memprint list yang tidak ditambahkan masukan user
                                break # mengakhiri for looping
                            else: # jika input user tidak sama dengan 'y', 'Y', 'n', atau 'N'
                                print('The input is wrong, please try again') # memprint tanda notif bahwa input user salah
                                break # mengakhiri for looping
                elif var == 'vegetables': # sama dengan kode untuk fruits, tetapi variabel fruits diganti menjadi vegetables
                    edit = input('please input item you want to add:')
                    editx = edit.lower()
                    i = len(vegetables)
                    for n in range(0,i+1):
                        if n == i:
                            vegetables.append(editx)
                            print('The data that you input is saved')
                            print('vegetables:',vegetables)
                            break
                        elif editx == vegetables[n]:
                            create = str(input('The list already contained the data that you input, do you want to add it? (Y/N)'))
                            create2 = create.lower()
                            if create2 == 'y':
                                vegetables.append(editx)
                                print('The data that you input is saved')
                                print('vegetables:',vegetables)
                                break
                            elif create2 == 'n':
                                print('The data that you input is not saved')
                                print('vegetables:',vegetables)
                                break
                            else:
                                print('The input is wrong, please try again')
                                break
                elif var == 'instants': # sama dengan kode untuk fruits, tetapi variabel fruits diganti menjadi instants
                    edit = input('please input item you want to add:')  # mengeset variabel input bernama edit
                    editx = edit.lower() # variabel input edit yang di-lowercase
                    i = len(instants) # menghitung berapa banyak isi list fruits
                    for n in range(0,i+1):
                        if n == i:
                            instants.append(editx)
                            print('The data that you input is saved')
                            print('instants:',instants)
                            break
                        elif editx == instants[n]:
                            create = str(input('The list already contained the data that you input, do you want to add it? (Y/N)'))
                            create2 = create.lower()
                            if create2 == 'y':
                                instants.append(editx)
                                print('The data that you input is saved')
                                print('instants:',instants)
                                break
                            elif create2 == 'n':
                                print('The data that you input is not saved')
                                print('instants:',instants)
                                break
                            else:
                                print('The input is wrong, please try again')
                                break
                else: # jika input user bukan fruits, vegetables, atau instants
                    print('none in log')

            elif opsiuser == '3': # opsi untuk menghapus isi list berdasarkan input user
                print('=== REMOVE LOG ===')
                var = input('fruits/vegetables/instants:') # user memasukkan input list mana yang isinya akan dihapus
                if var == 'fruits':
                    x = input('[1] Remove the whole list \n[2] Remove item on the list \n[1/2]:')
                    if x == '1':
                        fruits.clear()
                        print('fruits:', fruits)
                    elif x == '2':
                        i = len(fruits) # menghitung total jumlah isi list
                        j = i - 1 # mengeset variabel
                        k = j # mengeset variabel
                        n = 0 # mengeset variabel
                        edit = input('please input the item that you want to remove: ') # input yang dimasukkan user
                        editx = edit.lower() # input user yang dibuat menjadi lowercase seandainya user memasukkan huruf kapital/besar

                        while n <= j: # while digunakan karena variabel pembatas loop dapat disesuaikan dengan kebutuhan, berbeda dengan for ... in ... yang pembatas loopnya fixed
                            if editx == fruits[n]: # mengecek apakah input user ada di index dalam daftar
                                fruits.remove(editx) # jika kondisi terpenuhi, isi index dalam daftar tersebut dihapus
                                j -= 1 # nilai j digeser karena setelah command remove, ada pergeseran index yang berkurang sebesar 1, misal: daftar[0] yang baru berasal dari daftar[1] sebelumnya, dst
                                n = 0 # untuk mengulang proses looping, nilai n diset 0 agar pengecekan dimulai dari daftar[0] yang baru
                            elif n == j and j == k: # mengecek apakah nilai n sudah sama dengan j dan apakah nilai j ada perubahan atau tidak
                                print('The data that you input does not exist in the list') # jika kondisi memenuhi, berarti tidak ada perubahan daftar; dengan kata lain, input tidak eksis di daftar
                                break # proses looping diakhiri 
                            else: # jika tidak ada data yang dihapus, variabel n bertambah 1 (n = n + 1)
                                n += 1 
                        print('fruits:',fruits)


                elif var == 'vegetables':
                    x = input('[1] Remove the whole list \n[2] Remove item on the list \n[1/2]:')
                    if x == '1':
                        vegetables.clear()
                        print('Vegetables:', vegetables)
                    elif x == '2':
                        i = len(vegetables) # menghitung total jumlah isi list
                        j = i - 1 # mengeset variabel
                        k = j # mengeset variabel
                        n = 0 # mengeset variabel
                        edit = input('please input the item that you want to remove: ') # input yang dimasukkan user
                        editx = edit.lower() # input user yang dibuat menjadi lowercase seandainya user memasukkan huruf kapital/besar

                        while n <= j: # while digunakan karena variabel pembatas loop dapat disesuaikan dengan kebutuhan, berbeda dengan for ... in ... yang pembatas loopnya fixed
                            if editx == vegetables[n]: # mengecek apakah input user ada di index dalam daftar
                                vegetables.remove(editx) # jika kondisi terpenuhi, isi index dalam daftar tersebut dihapus
                                j -= 1 # nilai j digeser karena setelah command remove, ada pergeseran index yang berkurang sebesar 1, misal: daftar[0] yang baru berasal dari daftar[1] sebelumnya, dst
                                n = 0 # untuk mengulang proses looping, nilai n diset 0 agar pengecekan dimulai dari daftar[0] yang baru
                            elif n == j and j == k: # mengecek apakah nilai n sudah sama dengan j dan apakah nilai j ada perubahan atau tidak
                                print('The data that you input does not exist in the list') # jika kondisi memenuhi, berarti tidak ada perubahan daftar; dengan kata lain, input tidak eksis di daftar
                                break # proses looping diakhiri 
                            else: # jika tidak ada data yang dihapus, variabel n bertambah 1 (n = n + 1)
                                n += 1 
                        print('vegetables: ',vegetables)

                elif var == 'instants':
                    x = input('[1] Remove the whole list \n[2] Remove item on the list \n[1/2]:')
                    if x == '1':
                        instants.clear()
                        print('Instants:', instants)
                    elif x == '2':
                        i = len(instants) # menghitung berapa banyak isi list
                        j = i - 1 # mengeset variabel
                        k = j # mengeset variabel
                        n = 0 # mengeset variabel
                        edit = input('please input the item that you want to remove: ') # input yang dimasukkan user
                        editx = edit.lower() # input user yang dibuat menjadi lowercase seandainya user memasukkan huruf kapital/besar

                        while n <= j: # while digunakan karena variabel pembatas loop dapat disesuaikan dengan kebutuhan, berbeda dengan for ... in ... yang pembatas loopnya fixed
                            if editx == instants[n]: # mengecek apakah input user ada di index dalam daftar
                                instants.remove(editx) # jika kondisi terpenuhi, isi index dalam daftar tersebut dihapus
                                j -= 1 # nilai j digeser karena setelah command remove, ada pergeseran index yang berkurang sebesar 1, misal: daftar[0] yang baru berasal dari daftar[1] sebelumnya, dst
                                n = 0 # untuk mengulang proses looping, nilai n diset 0 agar pengecekan dimulai dari daftar[0] yang baru
                            elif n == j and j == k: # mengecek apakah nilai n sudah sama dengan j dan apakah nilai j ada perubahan atau tidak
                                print('The data that you input does not exist in the list') # jika kondisi memenuhi, berarti tidak ada perubahan daftar; dengan kata lain, input tidak eksis di daftar
                                break # proses looping diakhiri 
                            else: # jika tidak ada data yang dihapus, variabel n bertambah 1 (n = n + 1)
                                n += 1 
                        print('instants: ',instants)
                else: # jika input user bukan fruits, vegetables, atau instants
                    print('none in log')

            elif opsiuser == '4': # jika user memilih input untuk opsi mengupdate/mengubah isi list
                print('=== UPDATE LOG ===')
                var = input('fruits/vegetables/instants: ') # user memasukkan input list mana yang isinya akan diubah
                if var == 'fruits': # jika user memilih list fruits
                    upd = input('please input item that you want to change/update: ').lower() # user memasukkan nama dari list fruits yang akan digantikan
                    i = len(fruits) # menghitung berapa banyak isi list
                    for n in range(0,i+1): # mengeset looping for dengan variabel n sebagai variabel penentu dan batasnya ditentukan variabel i
                        if n == i: # jika n telah bernilai sama dengan i
                            print('The data that you input does not exist in the list') # memprint notif bahwa input nama lama yang akan digantikan tidak ada di dalam daftar list
                            break # mengakhiri looping for
                        elif upd == fruits[n]: # jika input yang dimasukkan user adalah sama dengan isi index dari list yang diperiksa pada pengulangan ini
                            upd1 = input('please input the new name for the item: ').lower() # user memasukkan nama baru yang akan menggantikan isi list lama
                            fruits[n] = upd1 # isi index dari list akan diubah menjadi nama yang baru
                            break # mengakhiri looping for
                    print('fruits: ',fruits)    
                
                elif var == 'vegetables': # sama dengan kode untuk fruits, tetapi variabel fruits diganti menjadi vegetables
                    upd = input('please input item that you want to change/update: ').lower()
                    i = len(vegetables)
                    for n in range(0,i+1):
                        if n == i:
                            print('The data that you input does not exist in the list')
                            break
                        elif upd == vegetables[n]:
                            upd1 = input('please input the new name for the item: ').lower()
                            vegetables[n] = upd1
                            break
                    print('vegetables: ',vegetables)  
                elif var == 'instants': # sama dengan kode untuk fruits, tetapi variabel fruits diganti menjadi instants
                    upd = input('please input item that you want to change/update: ').lower()
                    i = len(instants)
                    for n in range(0,i+1):
                        if n == i:
                            print('The data that you input does not exist in the list')
                            break
                        elif upd == instants[n]:
                            upd1 = input('please input the new name for the item: ').lower()
                            instants[n] = upd1
                            break
                    print('instants: ',instants)
                else: # jika input user bukan fruits, vegetables, atau instants
                    print('none in log')
            elif opsiuser == '5': # jika user memilih opsi untuk exit
                opsi12 = False
            else: # jika user memilih input selain 1 - 5
                print('Your input is wrong, please input a number from 1 to 5')



    elif opsi == '13':
        print(' "ANDA TELAH BERHASIL KELUAR" ')
        break
    else:
        print('Pilihan yang anda masukkan salah!')
        
