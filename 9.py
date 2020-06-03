# ### Email Validation

# input :
# Masukkan : alamat email :

# Kondisi:
# - Memiliki format nama user@nama hosting.ekstensi (contoh: .com)
# - Nama user hanya boleh huruf, angka, underscore, dan titik
# - Nama hosting hanya boleh huruf dan angka 
# - nama ekstensi hanya boleh huruf dan maksimal 5 karakter

# Outputnya:
# Alamat email yang anda masukkan tidak valid 
# - Tidak valid karena format salah (tidak ada @ atau pakai ,)
# - Tidak valid karena user name yang anda masukkan salah
# - Tidak valid karena format hosting yang anda masukkan salah
# - Tidak valid karena format ekstensi yang anda masukkan salah

# Alamat email yang anda masukkan valid 

# Contoh:
# - Valid 
# andre@gmail.com 
# joni12@city.id 
# Joni234_andre@avenger25.space

# - Tidak valid:
# andre-^&*@gmail.com # memakai tanda - atau simbol2
# johny245@g_#$^mail.com
# 79andi@yahoo
# tony@avenger25.community

# Deadline Minggu malam dan kirim email

valid = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
         'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
          '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '_', '.'} # membuat set huruf, angka, underscore, dan titik untuk validitas user name
valid1 = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
          'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
          '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'} # membuat set huruf dan angka untuk validitas nama hosting
valid2 = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
          'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'} # membuat set huruf untuk validitas nama eksetensi

email = input('Silahkan memasukkan alamat email anda: ') # user memasukkan input alamat emailnya

emailcheck = email.split("@") # memecah alamat email user berpatokan dari tanda @ menjadi list berisikan dua index
x = 2 # variabel untuk mengecek apakah input user telah dipecah dengan sesuai atau tidak, bisa juga digunakan untuk mengecek nama hosting dan ekstensi
y = 5 # variabel untuk mengecek apakah input nama ekstensi user di atas 5 karakter atau tidak
A = True # variabel untuk mengecek apakah input yang dimasukkan email telah berhasil lolos dari pengecekan error username, nama hosting, dan ekstensi

if len(emailcheck) == x: # jika tanda @ telah diinput pada posisi dan jumlah yang benar, variabel berikutnya akan ditentukan
    hostingekstensi = emailcheck[1] # mengambil bagian nama hosting.ekstensi dari hasil pen-splitan tanda @
    hostingekstensi2 = hostingekstensi.split('.') # mensplit hosting.ekstensi menjadi list yang berisikan dua index terpisah, hosting dan ekstensi

usercheck1 = {} # mengeset variabel yang akan diisi dengan input user name sebagai set dengan isi kosong
hostingcheck1 = {} # mengeset variabel yang akan diisi dengan input hosting name sebagai set dengan isi kosong
ekstensicheck1 = {} # mengeset variabel yang akan diisi dengan input nama ekstensi sebagai set dengan isi kosong

if "@" not in email: # jika user tidak menginput tanda @, notif error akan diprint
    print('Email anda tidak valid karena alamat email anda tidak mengandung tanda @')
    A = False 
elif "." not in email: # jika user tidak menginput tanda titik (.), notif error akan diprint
    print('Email anda tidak valid karena alamat email anda tidak mengandung tanda titik (.)')
    A = False
elif len(emailcheck) != x: # jika user memasukkan tanda @ lebih dari satu, notif akan diprint
    print('Email anda tidak valid karena anda memasukkan tanda @ di bagian nama user, nama hosting, atau ekstensi anda ')
    A = False
elif len(hostingekstensi2) != x: # jika user menginput tanda titik lebih dari satu pada bagian nama hosting atau ekstensi
    print('Email anda tidak valid karena anda memasukkan tanda titik (.) lebih dari satu pada bagian nama hosting atau ekstensi')
    A = False
else:
    usercheck = emailcheck[0]  # mengambil nama user dari list hasil pen-splitan tanda @ 
    usercheck1 = set(usercheck) # karakter dari nama user akan diubah per karakter dalam bentuk set, karakter duplikat otomatis akan terhapus
    hostingcheck = hostingekstensi2[0] # mengambil nama hosting dari list hasil pen-splitan tanda titik
    hostingcheck1 = set(hostingcheck) # karakter dari nama hosting akan diubah per karakter dalam bentuk set, karakter duplikat otomatis akan terhapus
    ekstensicheck = hostingekstensi2[1] # mengambil nama ekstensi dari list hasil pen-splitan tanda titik
    ekstensicheck1 = set(ekstensicheck) # karakter dari nama ekstensi akan diubah per karakter dalam bentuk set, karakter duplikat otomatis akan terhapus

for usersaja in usercheck1: # mengeset looping for dengan variabel usersaja yang nilainya mengandung semua karakter di bagian user name yang diinput user
    if usersaja not in valid: # jika nama user tidak terdaftar di set 'valid', notif akan diprint
        print('Email anda tidak valid karena nama user anda hanya dapat menampung karakter huruf alfabet (a - z), angka (0 - 9), underscore (_), atau titik (.)')
        A = False
        break # keluar dari looping for    


for hostingsaja in hostingcheck1: # mengeset looping for dengan variabel hostingsaja yang nilainya mengandung semua karakter di bagian hosting name yang diinput user
    if hostingsaja not in valid1: # jika nama hosting tidak terdaftar di set 'valid1', notif akan diprint
        print('Email anda tidak valid karena nama hosting anda hanya dapat menampung karakter huruf alfabet (a - z) atau angka (0 - 9)')
        A = False
        break # keluar dari looping for

for ekstensisaja in ekstensicheck1: # mengeset looping for dengan variabel ekstensisaja yang nilainya mengandung semua karakter di bagian nama ekstensi yang diinput user
    if ekstensisaja not in valid2: # jika nama ekstensi tidak terdaftar di set 'valid2', notif akan diprint
        print('Email anda tidak valid karena nama ekstensi anda hanya dapat menampung karakter huruf alfabet (a - z)')
        A = False
        break # keluar dari looping for
    elif len(ekstensicheck) > y: # jika panjang karakter nama ekstensi lebih dari 5, akan diprint notif
        print('Email anda tidak valid karena panjang nama ekstensi anda lebih dari 5')
        A = False
        break # keluar dari looping for

if A == True: # jika user tidak mendapatkan notif error, akan diprint notif berikut
    print('Email anda valid')     