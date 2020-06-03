### Lambda, Map dan Filter

# Lambda -  Anonymous function, one time use, small size
# Basic syntax

a = lambda argumen: print(argumen) # lambda dapat memiliki banyak argumen, tetapi hanya dapat memiliki 1 expression/fungsi/program

# a("Selamat Pagi")

# print(a)


kuadrat = lambda x: x ** 2

# print(kuadrat(5))

def kuadrat2(x):
    return x ** 2

# print(kuadrat2(5))

pangkat = lambda x, y: x ** y

# print(pangkat(5, 3))

cek = lambda x: True if x%2 == 0 else False

# print(cek(39))
# print(cek(80))

cek2 = lambda x: "Angka Genap" if x%2 == 0 else "Angka Ganjil"

# print(cek2(39))
# print(cek2(80))

genap = []
ganjil = []

cek3 = lambda x: genap.append(x) if x%2 == 0 else ganjil.append(x)

# print(cek3(59))
# print(genap)
# print(ganjil)

#### Map, hasil dari map function berupa object map sehingga tidak dapat diakses by index maupun len atau melihat isinya
### harus dikonversi
### Basic Syntax nya
### Data iterables = list, tuple, dict, dll
# map(function, data iterables) ## function 1, data iterables banyaknya sesuai dg banyaknya argumen di dalam function

a = [1,2,3,4,5]
b = []
# print(kuadrat2(5))

for i in a:
    b.append(kuadrat2(i))
# print(b)
c = list(map(kuadrat2, a))
# print(c)

def pangkat2(x, y):
    return x ** y

# pangkat2(a, c)

d = list(map(pangkat2, a, c))

# print(d)

e = list(map(pangkat2, a, list(map(kuadrat2, a))))
# print(e)


# def kuadrat2(x):
#     return x ** 2

kuadrat3 = lambda x: x ** 2
pangkat3 = lambda x, y: x ** y

kuadrat4 = lambda x: x ** 3

i = list(map(kuadrat4, a))

###################################
f = list(map(kuadrat3, a))


#########################################

# h = list(map(pangkat3, a, g))



# h1 = list(map(lambda x, y: x ** y, a, g))
############################################
g1 = list(map(lambda x: x ** 2, a))
i2 = list(map(lambda x: x ** 3, a))


h2 = list(map(lambda x, y: x ** y, list(map(lambda x: x**3, a)), list(map(lambda x: x ** 2, a))))

# print(f)
# print(g)
# print(h)
# print(h1)
# print(h2)
# print(i)
# print(i2)

jumlah = lambda x,y,z: x + y + z

k = list(map(jumlah, g1, i2, h2))


# print(k)

k2 = list(map(lambda x,y,z: x + y + z, g1, i2, h2))
# print(k2)

k3 =list(map(lambda x,y,z: x + y + z, list(map(lambda x: x ** 2, a)), list(map(lambda x: x ** 3, a)),list(map(lambda x, y: x ** y, list(map(lambda x: x**3, a)), list(map(lambda x: x ** 2, a))))))
# print(k3)

##### Filter ==== 
# Basic Syntax :
# filter(function, data iterable) # hasil dari filter adalah data yg bernilai TRUE berdasarkan function, Function berupa function - comparison atau pengujian kondisi
# hanya menerima 1 data iterables

## Map dan Filter menghasilkan Object, sehingga HARUS dikonversi
a = [1,2,3,4,5,6,7,8]


s = list(filter(lambda x: x%2 == 0, a))

print(s)

u = list(filter(lambda x: x%2 != 0, a))
print(u)




# genap = []
# ganjil = []

# map(lambda x: genap.append(x) if x%2 == 0 else ganjil.append(x), a)

# print(gh)
# print(genap)
# print(ganjil)

####### Reduce
## Basic Syntax
# menghasilkan 1 data ===
# faktorial 1 x 2 x 3 x 4 x 5
# Reduce(function, data iterables)

a = [1,2,3,4,5]
from functools import reduce

df = reduce(lambda x,y: 2*x + 2*y, a)

print(df)
##########
berapa jumlah total dari bilangan ganjil yang telah dipangkat 3 dari 1 - 200