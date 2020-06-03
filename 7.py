# Jawaban Latihan 6

# for i in range(5):
#     print(i)

# for i in range(1,6):
#     print(i)

# for i in range(5):
#     print(i+1)

# for i in range(1,6):
#     print(i * i)

# Jawaban nomor 1

# for i in range(1,6):
#     print(str(i) * i) # Tidak ada spasi

for i in range(1,6):
    print((str(i) + ' ') * i) 

print("=" * 100)

# Jawaban nomor 4
x = 6

for i in range(1,6):
    print((str(i) + ' ') * (x-i)) 

print("=" * 100)

# Jawaban nomor 2
# angka = ""
# for i in range(1,6):
#     angka = angka + str(i)
#     print(angka)

# iterasi pertama
# angka iterasi 1 = ""
# i = "1"
# angka = "" + "1"
# angka = "1"

# iterasi kedua
# i = "2"
# angka sebelumnya (iterasi 1) = "1"
# angka = "1" + "2"
# angka = "1 2"

# iterasi ketiga
# i = "3"
# angka = angka + "3"
# angka sebelumnya (iterasi 2) = "1 2"
# angka = "1 2" + "3"
# angka = "1 2 3"

# iterasi keempat
# i = "4"
# angka = angka + "3"
# angka sebelumnya (iterasi 3) = "1 2 3"
# angka = "1 2 3" + "4"
# angka = "1 2 3 4"

# iterasi kelima
# i = "5"
# angka = angka + "3"
# angka sebelumnya (iterasi 4) = "1 2 3 4"
# angka = "1 2 3 4" + "5"
# angka = "1 2 3 4 5"

# Bagaimana bila yang dicari adalah:
#          1
#        2 2
#      3 3 3
#    4 4 4 4
#  5 5 5 5 5

# for i in range(1,6):
#     print(' ' * (6 - i) + (str(i) + ' ') * i) # bentuk setengah diamond atas ke bawah

# for i in range(1,6):
#     print('  ' * (6 - i) + ((str(i) + ' ') * i)) # pada spasi yang pertama dituliskan dua kali, jadi '  ' bukan ' '

# z = ''
# for item in range(7):
#     for item1 in range(10):
#         z += str(item1)
#     z += '\n'
# print(z)

# for i in range(6):
#     print(i)
#     print("Data pengulangan")

# Contoh lain dari jawaban untuk latihan nomor 2
# angka = ""
# for i in range(1,6):
#     angka = angka + str(i)

# print(angka) # hanya memprint hasil pada pengulangan terakhir dari looping for

# Kode Bu Andita untuk leatihan tentang himpunan bilangan prima
# x = 1
# y = 21
# D = []
# for d in range(x,y): # dari 1 sampai 20 d adalah angka 1 - 20
#     if d > 1:
#         for n in range(2, d):
#             if d%n == 0:
#                 break # perintah break tidak melanjutkan ke else:
#         else:
#             D.append(d)
# print("Bilangan Prima")
# print(D)

# iterasi kedua 
# d = 2
# for n in range(2,2): # pengulangan pada iterasi kedua diabaikan, sudah terjadi tetapi tidak dilakukan apa2
#   print(n)

# for i in range(5):
#     pass # pengulangan sudah terjadi tetapi tidak dilakukan apa2 
# else:
#     print("Pengulangan selesai")

# for d in range(x,y): # dari 1 sampai 20 d adalah angka 1 - 20
#     if d > 1:
#         for n in range(2, d):
#             if d%n == 0:
#                 break # perintah break tidak melanjutkan ke else:
#         #else:
#             D.append(d)
# print("Bilangan Prima")
# print(D)
# Else akan dirun ketika seluruh iterasi selesai dan dirun  satu kali (iterasi selesai tanpa interupsi break)

# Hasil akhir adalah beberapa angka ada yang diulang banyak dan angka 9 (bukan prima) dimasukkan

# pada iterasi ke-9
# D = []
# for n in range(2,9):
#     if 9%n == 0:
#        break
#     D.append(9)

# print(D)

# iterasi pertama
# n = 2
# if 9%2 == 0 # hasil False, perintah IF tidak dijalankan
# perintah Append dijalankan 

# D = []
# for n in range(2,5): ### 2, 3, 4
#     if 5%n == 0:
#        break
#     D.append(5)

# print(D)

# iterasi pertama
# n = 2
# if 5%2 == 0 # hasil False, perintah IF tidak dijalankan
# perintah di bawah IF dijalankan (perintah Append)

# iterasi kedua
# n = 3
# if 5%3 == 0: # False, IF tidak dijalankan 
# perintah di bawah IF dijalankan (perintah Append)

# iterasi ketiga
# n = 4
# if 5%4 == 0: # False, IF tidak dijalankan 
# perintah di bawah IF dijalankan (perintah Append)

# nilai d = 7
# iterasi pertama 
# 7%2
# karena IF (Break) tidak dijalankan selama proses iterasi, maka Else akan dijalankan karena proses iterasi telah selesai

# for i in range(5):
#     print("pengulangan")
# else: # else hanya dijalankan sekali setelah perintah for selesai looping
#     print("Pengulangan selesai")

# for i in range(2,21):
#     print("pengulangan")
#     break
# else: # else hanya dijalankan sekali setelah perintah for selesai looping, tetapi karena ada break, perintah for diputus sedangkan else ada di perintah for sehingga else tidak dijalankan
#     print("Pengulangan selesai")

# break = untuk melakukan interupsi terhadap Looping (menghentikan looping)

# pass = untuk construct program

# Dengan while, membuat
# 1
# 22
# 333
# 4444
# 55555

# i = 1
# while i < 6:
#     print(str(i) * i)
#     i += 1

# Alternatif nomor 2 dengan nested for
for i in range(1,6):
    for j in range(1,i+1):
        print((str(i) + ' ') * i)
        break

# Alternatif nomor 7 versi Bu Citra
z = ''
for i in range(0,6):
    for j in range(0, 5 - i):
        z += '   '
    for k in range(1, 2 * i): 
        z += ' * '
    z += '\n'
for a in range(0,5):
    for c in range(0, a):
        z += '   '
    for b in range(1, (5 * 2) - 2 * a):
        z += ' * '
    z += '\n'
print(z)

# = adalah assignment operator

# 1+1
# 2+1
# 3-1
# 5*4
# 2/1
# angka = 4

# angka = angka + 5
# mempersingkat 
# angka += 5 # bisa digunakan bila variabel angka sudah didefine terlebih dahulu

# angka = angka / 5
# angka /= 5

# Latihan:
# input : masukan kalimat

# outputnya : kata dalam kalimat dibalik

# misalnya, input : "nama saya joni"
# outputnya: "aman ayas inoj"