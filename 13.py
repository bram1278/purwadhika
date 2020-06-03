### Review

# Tipe Data Primitif
# integer - string - boolean - float - complex number

# Print
# print("Hello")
# print('Hello')
# print('''Hello''')

# print(9) # integer
# print(9.5) # float

# print(True) # boolean

# # Var
# # list str int float (reserve word)

# # Assignment Operator (=) untuk memasukkan nilai ke suatu variabel

# a = 5
# nama = "Andi"

# # Math Operator
# print(5 + 5)
# print(5 * 5)
# print(5 / 5) #### hasil pembagian pasti dalam format float
# print(5 - 5)
# print(int(5/2)) #### hasil pembagian pasti dalam format integer (pembulatan ke bawah)
# print(5 // 2) ##### hasil pembagian pasti dalam format integer (pembulatan ke bawah)
# print(round(5/2)) 

# round(angka, jumlah desimal)

# print(round(2.5)) # tidak ada koma desimal, nilai 2
# print(round(3.5)) # tidak ada koma desimal, nilai 4
# ketika angka di depan koma adalah genap, pembulatan round turun ke bawah 
# ketika angka di depan koma adalah ganjil, pembulatan round naik ke atas

# print(5 % 2) # diprint sisa pembagian yang bernilai 1
# print(1 % 2) # diprint 1

# Operator gabungan
# a = 5

# a = a + 8
# print(a)
# a += 8 # bisa juga untuk pengurangan, perkalian, pembagian termasuk modulus (%=) jika variabel sudah didefinisikan
# print(a)


# fungsi ubah tipe data
# int(), str(), float()

# input 
# s = input("masukkan no ") # hasil dari fungsi input adalah dalam format string, meskipun yang dimasukkan adalah angka

# print(type(s))

# .lower() # lowercase
# .upper() # uppercase
# .capitalize() # hanya huruf pertama pada kata pertama saja yang besar, 
# .title() # semua huruf pertama per kata dijadikan besar 

# s = "mangga besar"
# print(s.lower())
# print(s.upper())
# print(s.capitalize())
# print(s.title())

# Comparison = hasil TRUE and FALSE
# print(1 > 2)
# print(1 < 2)
# print(1 >= 2)
# print(1 <= 2)
# print(1 == 2)
# print(1 != 2)

# And dan Or
# And akan menghasilkan TRUE jika keduanya TRUE
# OR akan menghasilkan FALSE jika keduanya FALSE

# print((5 > 2) and (1 < 2))
# print((5 > 2) and (1 == 2))
# print((5 > 2) or (1 == 2))

# membership in dan not in untuk mengecek data iterable
# print( "a" in "hallo")
# print("t" in "hallo")
# print("t" not in "hallo")

# Identity : is dan is not
# print(5 is 5)
# print(5 == 5)

### 
# .isdigit, .isalpha, .isalnum # hasilnya pasti boolean, TRUE atau FALSE
# s = "582"
# print(s.isdigit()) # hasilnya True
# print(int(s)) 

# s = "5 82"
# print(s.isdigit()) # hasilnya False karena spasi bukan digit
# print(int(s)) # error karena spasi (string) tidak bisa diubah menjadi integer

# s = "5.82"
# print(s.isdigit()) # hasilnya False
# print(int(s)) # error karena tanda titik (string) tidak bisa diubah menjadi integer

# t = 5.82
# print(int(t)) # float bisa diubah menjadi int asalkan nilainya True

# z = "an2di"
# print(z.isalpha()) # False
# print(z.isalnum()) # True

# Fungsi IF
# angka = 8
# if angka % 2 == 0:
#     print("Genap")
# else:
#     print("Ganjil")

# if .....:
#   pass
# if .....:
#   pass
# else:
#   pass

# if ....:
#   pass
# elif ....:
#   pass
# else:
#   pass

# a = [1,2,3,4,5]

# for i in a:
#     print(i)

# List Comprehension, membuat list baru dengan menggunakan expression
# list baru = [expression]

angka = [1, 2, 3, 4, 5]
pangkat = []
for i in angka:
    pangkat.append(i**2)
# print(pangkat)

pangkat2 = list(map(lambda x: x**2, angka))
# print(pangkat2)

######
pangkat3 = [i**2 for i in angka]
# print(pangkat3)

a = [1, 2, 3, 4]
b = [2, 4, 5, 7]

sama = []
for i in a:
    for j in b:
        if i == j:
            sama.append(i)

print(sama)

sama2 = [i for i in a for j in b if i == j]
print(sama2)

# buah = ["mangga", "jeruk", "apel", "alpukat"]
# kombinasi = ["susu", "keju", "coklat", "apel", "mangga"]
# gunakan list comprehension
# (mangga,susu), (mangga, keju), (mangga, coklat) ..... tapi tak ada yg sama
# (mangga, mangga) tak ada
# (apel, apel) tak ada
###############################################

# kombo = [ [i**2, i**3] for i in a]

# print(kombo)

kombo = [ (i**2, i**3) for i in a]

print(kombo)

buah = ["mangga", "jeruk", "apel", "alpukat"]
kombinasi = ["susu", "keju", "coklat", "apel", "mangga"]
new = [(i,j) for i in buah for j in kombinasi if i != j]
print(new)