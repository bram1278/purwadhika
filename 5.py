## list, tuple

## set 
# sifatnya unordered, tidak seperti index (no indexing), setiap datanya unique (jika ada data duplikat, dihitung hanya satu)

data = {5,8,'nama',9} # kurungnya kurawal

# print(data)

# data = {5,8,'nama',9, ['andi', 'deni']} 
# print(data)

# data = {5,8,'nama',9, ('andi', 'deni'), 9, 8}
# print(data)

angka = [5,7,8,9,8,9,5,5,7,8,9,8,9,5,5,7,8,9,8,9,5,5,7,8,9,8,9,5]
# data1 = set(angka)
# print (angka)
# print(data1)

# kalimat.replace(nama,namabaru)

data1 = set([5,8,9,10,5,8,6])

data2 = set([5,8,9,2,1,4])
# print(data1)
# print(8 in data1)

# data1.update('andi')
# print(data1) # diupdate per karakter 'a', 'n, 'd', 'i'

# data1.update(['andi'])
# data1.update(('andre')) # tupple akan diupdate per karakter

# data1.update(['andre']) # tupplenya perlu diubah menjadi list

# data1.add(angka) # error karena dalam bentuk list

# data1.add(tuple(angka))
# print(data1)

siswa = ['joni', 'budi', 'doni', 'eka', 'nisa']

# data1.update(('andri')) # untuk tuple, huruf akan dipecah per karakter
# data1.update('andri')
# data1.add('andi')
# data1.add(siswa) # error karena tidak bisa add list
# data1.update(siswa)
# print(data1)

# print(data1.update("andi")) # hasilnya none karena print dan update tidak bisa dalam satu fungsi

# hapus data
# data1.remove('andi')
# data1.discard('budi')

# data1.remove('jen') # error karena di data1, tidak ada variabel jen. Error if data not exist
# data1.discard('jen') # no error even if data not exist

# hapus seluruh data
# data1.clear() # menghapus seluruh data di data1

# del data1 # error karena data1 telah di-clear
# print(data1)

x = {1,2,3,4,5}
y = {1,2,3,8,7}

## UNION

print(x.union(y)) # himpunan matematika union

z = x.union(y)
# z = x.remove(3) # fungsi bisa diprint dan bisa assign value sedangkan method (contoh: update atau remove) tidak bisa sehingga hasilnya none

print(z)

print(x | y) # fungsi x union y
print(y | x) # fungsi y union x

## irisan - intersection

print(x.intersection(y))
print(y.intersection(x))

print(x & y) # fungsi x intersection y
print(y & x) # fungsi y intersection x

## Difference 

print(x.difference(y))
print(y.difference(x))

print(x - y) # fungsi x difference y 
print(y - x) # fungsi y difference x

## Symetric Difference (gabungan dari difference)
print(x.symmetric_difference(y))
print(y.symmetric_difference(x))

print(x ^ y) # fungsi x symetric difference y
print(y ^ x) # fungsi y symetric difference x

# Latihan: 
# A = himpunan bilangan genap dari 1 - 20
# B = himpunan bilangan ganjil dari 1 - 20
# C = himpunan bilangan negatif lebih dari -20; misal: -19, -18, ...
# D = himpunan bilangan prima dari 1 - 20
# E = himpunan bilangan komposit dari 1 - 20
# Bilangan komposit = bukan bilangan prima

# Output :
# a. A union B union C union D union E

# b. (A irisan B) union (D irisan E)
# 
# c. (A union B) irisan (D union E)
# 
# d. (A union B) - (D union E)
# 
# e. (A union B union C) - (A irisan E) 

# kalau bisa pembuatan himpunan menggunakan fungsi