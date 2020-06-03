# Lat 1:
# Buat algoritma ---
# buat List
# Pilihan:
# 1 = ascending (a - z) dari kecil ke besar
# 2 = descending(z - a) dari yang terbesar ke terkecil
# reverse, ::-1
# Output: sesuai Pilihan

alfabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] # list berisi urutan alfabet
angka = int(input('Silahkan masukkan angka 1 (mengurutkan secara ascending a - z) atau 2 (mengurutkan secara descending z - a): '))

if angka == 1 : # mengurutkan secara ascending
    print(f"Deretan alfabet yang diurutkan secara ascending adalah : \n {alfabet}")
elif angka == 2 : # mengurutkan secara descending
    alfabet.reverse()     
    print(f"Deretan alfabet yang diurutkan secara descending adalah : \n {alfabet}") 
else:
    print("Inputan anda salah, masukkan angka 1 atau 2")

# # Lat 2
# Buat algoritma
# cari nilai maksimal dan nilai minimal

daftar = [70, 80, 60, 70, 70, 80, 60, 50, 10, 70, 90, 90, 100, 20, 50, 60, 70, 80, 30, 40] # contoh list nilai dari satu kelas yang berjumlah 20 murid 

maksimum = max(daftar) # karena jika dimasukkan max(b), angka yang diprint bukan angka paling besar
minimum = min(daftar) # karena jika dimasukkan max(b), angka yang diprint bukan angka paling kecil

print(f"Nilai maksimum dari list 'daftar' adalah {maksimum} sedangkan nilai minimumnya adalah {minimum}")

# # Lat 3
# Buat algoritma
# Buat list
# cari :
# Modus : nilai yang paling sering muncul
# Median : Nilai tengah
# Mean : rata-rata
# Q1 : Quartal 1 atau 25 %
# Q3 : Quartal 3 atau 75 %
# Outliers

daftar = [70, 80, 60, 70, 70, 80, 60, 50, 10, 70, 90, 90, 100, 20, 50, 60, 70, 80, 30, 40] # contoh list nilai dari satu kelas yang berjumlah 20 murid 
daftar1 = [80, 50, 100, 90, 80, 10, 70, 40, 80, 100, 20, 70, 80, 50, 60] # contoh list nilai dari satu kelas yang berjumlah 15 murid 

daftarurut = sorted(daftar)
daftarurut1 = sorted(daftar1)
x = int(len(daftarurut))
x1 = int(len(daftarurut1))
 
mean = sum(daftarurut) / x
mean1 = sum(daftarurut1) / x1

print(f"Nilai mean dari list 'daftar' adalah {mean} ")
print(f"Nilai mean dari list 'daftar1' adalah {mean1} ")

if len(daftarurut)%2 == 0: # jika daftar memiliki jumlah murid genap 
    median1 = daftarurut[x//2] # tanda // digunakan karena hasil pembagiannya harus bertipe integer, tidak bisa float
    median2 = daftarurut[(x//2)+1] # tanda // digunakan karena hasil pembagiannya harus bertipe integer, tidak bisa float
    median = (median1 + median2)/2
elif len(daftarurut)%2 != 0: # jika daftar memiliki jumlah murid ganjil
    median = daftarurut[(x+1)//2] # tanda // digunakan karena hasil pembagiannya harus bertipe integer, tidak bisa float

if len(daftarurut1)%2 == 0: # jika daftar1 memiliki jumlah murid genap 
    median1a = daftarurut1[x1//2] # tanda // digunakan karena hasil pembagiannya harus bertipe integer, tidak bisa float
    median2a = daftarurut1[(x1//2)+1] # tanda // digunakan karena hasil pembagiannya harus bertipe integer, tidak bisa float
    median0a = (median1a + median2a)/2
elif len(daftarurut1)%2 != 0: # jika daftar1 memiliki jumlah murid ganjil
    median0a = daftarurut1[(x1+1)//2] # tanda // digunakan karena hasil pembagiannya harus bertipe integer, tidak bisa float

print(f"Nilai median dari list 'daftar' adalah {median} ")
print(f"Nilai median dari list 'daftar1' adalah {median0a} ")

daftarset = set (daftar) # mengubah list "daftar" menjadi format set untuk mengeliminasi data duplikat
daftarset1 = sorted(daftarset) # mengurutkan variabel "daftarset" dari nilai terendah hingga nilai tertinggi dalam format list
y = len(daftarset1)
counter1 = [] # variabel counter1 adalah list kosong yang akan digunakan ketika menghitung modulus daftar 

for i in range(0,y): # Loop for untuk menghitung modulus daftar
    counter = daftar.count(daftarset1[i]) # counter menghitung berapa jumlah pengulangan daftarset[i] yang sedang diperiksa di looping for saat ini    
    counter1.append(counter) # memasukkan nilai counter kepada list counter1
    if i == 0:
        modulus = daftarset1[i] # pada awal loop for, nilai modulus diisi sebagai nilai index dari daftarset1[0]   
    elif i > 0 and counter1[i] > counter1[i-1]:
        modulus = daftarset1[i] # jika nilai i > 0 dan nilai counter[i] saat ini lebih besar dari nilai counter [i-1], nilai modulus diubah menjadi daftarset1[i] saat ini   

daftarset0a = set (daftar1) # mengubah list "daftar1" menjadi format set untuk mengeliminasi data duplikat
daftarset1a = sorted(daftarset0a) # mengurutkan variabel "daftarset0a" dari nilai terendah hingga nilai tertinggi dalam format list
y1 = len(daftarset1a)
counter1a = [] # variabel counter1a adalah list kosong yang akan digunakan ketika menghitung modulus  daftar1

for i in range(0,y1): # Loop for untuk menghitung modulus daftar
    counter = daftar1.count(daftarset1a[i]) # counter menghitung berapa jumlah pengulangan daftarset[i] yang sedang diperiksa di looping for saat ini   
    counter1.append(counter) # memasukkan nilai counter kepada list counter1
    if i == 0:
        modulus1 = daftarset1a[i] # pada awal loop for, nilai modulus diisi sebagai nilai index dari daftarset1[0]   
    elif i > 0 and counter1[i] > counter1[i-1]:
        modulus1 = daftarset1a[i] # jika nilai i > 0 dan nilai counter[i] saat ini lebih besar dari nilai counter [i-1], nilai modulus diubah menjadi daftarset1[i] saat ini   

print(f"Nilai modulus dari list 'daftar' adalah {modulus} ")
print(f"Nilai modulus dari list 'daftar1' adalah {modulus1} ")

daftarq1ganjil = [] # membuat variabel daftarq1ganjil yang akan diisikan dengan nilai q1 jika list "daftar" memiliki jumlah index ganjil
daftarq1genap = [] # membuat variabel daftarq1genap yang akan diisikan dengan nilai q1 jika list "daftar" memiliki jumlah index genap
daftarq3ganjil = [] # membuat variabel daftarq3ganjil yang akan diisikan dengan nilai q3 jika list "daftar" memiliki jumlah index ganjil
daftarq3genap = [] # membuat variabel daftarq3genap yang akan diisikan dengan nilai q3 jika list "daftar" memiliki jumlah index genap

if x%2 == 0: # jika daftar memiliki jumlah murid genap 
    for i in range(0,x//2): # fungsi for untuk memasukkan nilai q1 genap
        daftarq1genap.append(daftarurut[i])        
    for i in range((x//2)+1,(x+1)): # fungsi for untuk memasukkan nilai q3 genap
        daftarq3genap.append(daftarurut[i-1])     
elif x%2 != 0: # jika daftar memiliki jumlah murid ganjil
    for i in range(0,(x+1)//2): # fungsi for untuk memasukkan nilai q1 ganjil
        daftarq1ganjil.append(daftarurut[i])
    for i in range((x+1)//2, (x+1)): # fungsi for untuk memasukkan nilai q3 ganjil
        daftarq3ganjil.append(daftarurut[i-1])

xq1genap = len(daftarq1genap) # menghitung berapa banyak index yang ada di list daftarq1genap
xq1ganjil = len(daftarq1ganjil) # menghitung berapa banyak index yang ada di list daftarq1ganjil
xq3genap = len(daftarq3genap) # menghitung berapa banyak index yang ada di list daftarq3genap
xq3ganjil = len(daftarq3ganjil) # menghitung berapa banyak index yang ada di list daftarq3ganjil

daftarq1ganjil1 = [] # membuat variabel daftarq1ganjil yang akan diisikan dengan nilai q1 jika list "daftar1" memiliki jumlah index ganjil
daftarq1genap1 = [] # membuat variabel daftarq1genap yang akan diisikan dengan nilai q1 jika list "daftar1" memiliki jumlah index genap
daftarq3ganjil1 = [] # membuat variabel daftarq3ganjil yang akan diisikan dengan nilai q3 jika list "daftar1" memiliki jumlah index ganjil
daftarq3genap1 = [] # membuat variabel daftarq3genap yang akan diisikan dengan nilai q3 jika list "daftar1" memiliki jumlah index genap  

if x1%2 == 0: # jika daftar memiliki jumlah murid genap 
    for i in range(0,x1//2): # fungsi for untuk memasukkan nilai q1 genap
        daftarq1genap1.append(daftarurut1[i])        
    for i in range((x1//2)+1,(x1+1)): # fungsi for untuk memasukkan nilai q3 genap
        daftarq3genap1.append(daftarurut1[i-1])     
elif x1%2 != 0: # jika daftar memiliki jumlah murid ganjil
    for i in range(0,(x1+1)//2): # fungsi for untuk memasukkan nilai q1 ganjil
        daftarq1ganjil1.append(daftarurut1[i])
    for i in range((x1+1)//2, (x1+1)): # fungsi for untuk memasukkan nilai q3 ganjil
        daftarq3ganjil1.append(daftarurut1[i-1])

xq1genap1 = len(daftarq1genap1) # menghitung berapa banyak index yang ada di list daftarq1genap
xq1ganjil1 = len(daftarq1ganjil1) # menghitung berapa banyak index yang ada di list daftarq1ganjil
xq3genap1 = len(daftarq3genap1) # menghitung berapa banyak index yang ada di list daftarq3genap
xq3ganjil1 = len(daftarq3ganjil1) # menghitung berapa banyak index yang ada di list daftarq3ganjil

if xq1genap != 0: 
    if xq1genap%2 == 0: # jika daftarq1genap memiliki index yang banyaknya genap
        q11 = daftarq1genap[xq1genap//2]
        q12 = daftarq1genap[(xq1genap//2)+1]
        q1 = (q11 + q12)/2
    elif xq1genap%2 != 0: # jika daftarq1genap memiliki index yang banyaknya ganjil
        q1 = daftarq1genap[(xq1genap+1)//2]

if xq1ganjil != 0:
    if xq1ganjil%2 == 0: # jika daftarq1ganjil memiliki index yang banyaknya genap
        q11 = daftarq1ganjil[xq1ganjil//2]
        q12 = daftarq1ganjil[(xq1ganjil//2)+1]
        q1 = (q11 + q12)/2
    elif xq1ganjil%2 != 0: # jika daftarq1ganjil memiliki index yang banyaknya ganjil
        q1 = daftarq1ganjil[(xq1ganjil+1)//2]

if xq1genap1 != 0:
    if xq1genap1%2 == 0: # jika daftarq1genap1 memiliki index yang banyaknya genap
        q11 = daftarq1genap1[xq1genap1//2]
        q12 = daftarq1genap1[(xq1genap1//2)+1]
        q1a = (q11 + q12)/2
    elif xq1genap1%2 != 0: # jika daftarq1genap1 memiliki index yang banyaknya ganjil
        q1a = daftarq1genap1[(xq1genap1+1)//2]

if xq1ganjil1 != 0:
    if xq1ganjil1%2 == 0: # jika daftarq1ganjil1 memiliki index yang banyaknya genap
        q11 = daftarq1ganjil1[xq1ganjil1//2]
        q12 = daftarq1ganjil1[(xq1ganjil1//2)+1]
        q1a = (q11 + q12)/2
    elif xq1ganjil1%2 != 0: # jika daftarq1ganjil1 memiliki index yang banyaknya ganjil
        q1a = daftarq1ganjil1[(xq1ganjil1+1)//2]

print(f"Nilai Q1 dari list 'daftar' adalah {q1} ")
print(f"Nilai Q1 dari list 'daftar1' adalah {q1a} ")

if xq3genap != 0: 
    if xq3genap%2 == 0: # jika daftarq3genap memiliki index yang banyaknya genap
        q31 = daftarq3genap[xq3genap//2]
        q32 = daftarq3genap[(xq3genap//2)+1]
        q3 = (q31 + q32)/2
    elif xq3genap%2 != 0: # jika daftarq1genap memiliki index yang banyaknya ganjil
        q3 = daftarq3genap[(xq3genap+1)//2]

if xq3ganjil != 0:
    if xq3ganjil%2 == 0: # jika daftarq3ganjil memiliki index yang banyaknya genap
        q31 = daftarq3ganjil[xq3ganjil//2]
        q32 = daftarq3ganjil[(xq3ganjil//2)+1]
        q3 = (q31 + q32)/2
    elif xq3ganjil%2 != 0: # jika daftarq3ganjil memiliki index yang banyaknya ganjil
        q3 = daftarq3ganjil[(xq3ganjil+1)//2]

if xq3genap1 != 0:
    if xq3genap1%2 == 0: # jika daftarq1genap1 memiliki index yang banyaknya genap
        q31 = daftarq3genap1[xq3genap1//2]
        q32 = daftarq3genap1[(xq3genap1//2)+1]
        q3a = (q31 + q32)/2
    elif xq3genap1%2 != 0: # jika daftarq1genap1 memiliki index yang banyaknya ganjil
        q3a = daftarq3genap1[(xq3genap1+1)//2]

if xq3ganjil1 != 0:
    if xq3ganjil1%2 == 0: # jika daftarq1ganjil1 memiliki index yang banyaknya genap
        q31 = daftarq3ganjil1[xq3ganjil1//2]
        q32 = daftarq3ganjil1[(xq3ganjil1//2)+1]
        q3a = (q31 + q32)/2
    elif xq3ganjil1%2 != 0: # jika daftarq1ganjil1 memiliki index yang banyaknya ganjil
        q3a = daftarq3ganjil1[(xq3ganjil1+1)//2]

print(f"Nilai Q3 dari list 'daftar' adalah {q3} ")
print(f"Nilai Q3 dari list 'daftar1' adalah {q3a} ")

iqr = q3 - q1 # nilai IQR (Interquartile Range) untuk list "daftar"
iqr1 = q3a - q1a # nilai IQR (Interquartile Range) untuk list "daftar1"
 
cekiqr1 = q1 - (1.5 * iqr)
cekiqr2 = q3 + (1.5 * iqr)
outliers = []

for i in range(0,x): # Loop for untuk menghitung nilai outliers
    if daftarurut[i] < cekiqr1 or daftarurut[i] > cekiqr2 :
        outliers.append(daftarurut[i])

cekiqr1a = q1a - (1.5 * iqr1)
cekiqr2a = q3a + (1.5 * iqr1)
outliers1 = []

for i in range(0,x1): # Loop for untuk menghitung nilai outliers
    if daftarurut1[i] < cekiqr1a or daftarurut1[i] > cekiqr2a :
        outliers1.append(daftarurut1[i])

print(f"Nilai outliers dari list 'daftar' adalah {outliers} ")
print(f"Nilai outliers dari list 'daftar1' adalah {outliers1} ")

# Latihan 4
# Buat def atau function
# Ada deret angka
# 1 2 3 4 5
# 6 7 8 9 10
# 11 12 13 14 15
# 16 17 18 19 20
# 21 22 23 24 25

# input : Spin ke : pilihan 1-4
# outputnya
# pilihan 1:
# 21 16 11 6 1
# 22 17 12 7 2
# 23 18 13 8 3
# 24 19 14 9 4
# 25 20 15 10 5

#pilihan 2:
# 25 24 23 22 21 
# 20 19 18 17 16
# 15 14 13 12 11
# 10 9 8 7 6
# 5 4 3 2 1

# pilihan 3:
# 5 10 15 20 25
# 4 9 14 19 24
# 3 8 13 18 23 
# 2 7 12 17 22
# 1 6 11 16 21

# pilihan 4
# 1 2 3 4 5
# 6 7 8 9 10
# 11 12 13 14 15
# 16 17 18 19 20
# 21 22 23 24 25

a = True
x = ''

def spin1(z):
    for i in range(21, 26):
            for j in range(0, 25, 5):
                z += str(i - j) + ' '
            z += '\n'
    return (z)

def spin2(z):
    for i in range(25, 0, -5):
        for j in range(i + 1, i - 4, -1):
            z += str(j - 1) + ' '
        z += '\n'
    return (z)

def spin3(z):
    for i in range(6, 1, -1):
        for j in range(0, 5):
            z += str(i - 1 + (5 * j)) + ' '
        z += '\n'
    return (z)

def spin4(z):
    for i in range(0, 25, 5):
        for j in range(i, i + 5):
            z += str(j + 1) + ' '
        z += '\n'
    return (z)

while a == True:
    angka = int(input('Silahkan masukkan angka 1 - 4 untuk memulai spin atau input lain untuk exit : '))
    if angka == 1:
        y = spin1(x)
        print(f"Hasil spin adalah :\n {y}")      
    elif angka == 2:
        y = spin2(x)
        print(f"Hasil spin adalah :\n {y}")   
    elif angka == 3:
        y = spin3(x)
        print(f"Hasil spin adalah :\n {y}")     
    elif angka == 4:
        y = spin4(x)
        print(f"Hasil spin adalah :\n {y}")    
    else:
        print("Exit")
        a = False