### Looping

# while dan for loop

# angka = 1

# while angka < 10 : 
#   print(angka)
#   angka += 1

# print('='*100)
# for i in range(1,10):
#   print(i)

# for i in range(1,9):
#     if i == 5:
#         break
#     print(i)
# print("ini di luar looping")

# print('='*100)

# for i in range(1,9):
#     print(i)
#     if i == 5:
#         break
# print("ini di luar looping")

# print('='*100)

# for i in range(1,10):
#     if i == 5:
#         continue
#     print(i)
# print("ini di luar looping")

# print('='*100)

# for i in range(1,10):
#     print(i)
#     if i == 5:
#         continue
# print("ini di luar looping")

# print('='*100)

#### Data Structure (data yang bisa diiterasi/ iterable data)
nilai = [8,9,10,110,20,85,10]

# print(nilai)

# for i in nilai:
#     print(i)

# slicing
# nilai[ start : end : step ]
# print(nilai[0]) 
# print(nilai[:]) # tanda : artinya dimulai dari indeks paling awal sampai paling akhir dengan step sebesar 1
# print(nilai[::-1]) # dimulai dari paling akhir sampai paling awal

# nilai.sort()
# print(nilai)

# namalist[index]

nilai.append(90) # data ditambahkan ke indeks paling akhir
# print(nilai)

nilai.insert(2,96) # nilai 96 dimasukkan ke indeks ke-2 (nilai[2])
# print(nilai)

print(nilai.index(110))

# print(nilai[9]) # error index out of range

# nilai.pop() # menghapus nilai untuk index terakhir

# print(nilai)

# nilai.pop(0) # menghapus nilai untuk index ke-0

# print(nilai)

# nilai.remove(10) # nilai 10 dihapus (jika ada data duplikasi, hanya nilai 10 yang pertama yang dihapus)
# print(nilai)

# j = 10
# for i in nilai:
#     if i == j:
#         nilai.remove(i)

# print(nilai)

nilai2 = [100,200,300]

nilai.append(nilai2) # list nilai2 ditambahkan sebagai list di dalam list nilai

print(nilai)

nilai.extend(nilai2) # setiap nilai dari list nilai2 dimasukkan ke list nilai (tak ada list di dalam list)

print(nilai)

## Tuple
# packing dan unpacking

a = 200
b = 300
c = 600
print(c)

a, b, c = 200, 300, 600 # multiple assignment
print(c)

d = 100, 1000, 2000 # packing == d adalah tuple

print(type(d)) # class d adalah tuple

f, g, h = 100, 1000, 2000

print(h)
print(len(d))
f, g, h = d # unpacking

print(h)

## set(), { data }
data = []
cek = ()
data_set = {} # tidak bisa digunakan untuk mendefinisikan set kosong karena sudah diprogram untuk dictionary

## dictionary
# dic = {keys : values, keys2: values2}

# dic[namakeys]

data = {"andi" : 80, "budi" : 90}

print(data["andi"])

### function def
# def nama fungsi ():
#   program (expression)

def salam(nama):
    print("selamat pagi",nama)

salam("andi")
salam("budi")

def jumlah(x, y):
    return x + y

d = jumlah(4,5)

print(d)
print(jumlah(4,5))

#### lambda, map, filter, reduce
# lambda argumen: expression # bisa banyak argumen tetapi hanya satu expression

pangkat = lambda x, y: x**y
print(pangkat(4,2))

### map

def pangkat2(x):
    return x**2

a = [2,5,6]
# print(pangkat2(a)) # error karena function tidak dapat memproses data structure/data iterable seperti list
for i in a:
    print(pangkat2(i))

b = [6]
hasil = list(map(pangkat,a,b))
print(hasil)
# map(function, data iterable) # jumlah data iterable sesuai dengan jumlah argumen
# filter(function, data iterable) # hanya mengambil value yang bernilai TRUE, jumlah data iterable hanya 1

### GitHub
# buat repo
# buka folder di VS Code
# ketika akan submit
# git init # dicetak di tampilan terminal
# git add . 
# git commit -m "catatan"
# git remote add origin (atau nama folder lain) https://github.com/kal172/project-kalkulator.git
# git 