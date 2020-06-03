## Data structured

## List, Tuple, Set

# A = [1,2,3]
# B = (1,2,3)
# C = {1,2,3}

## Dictionary, asosiasi, mapping

## Kamus
# kata : definisi
# keyword : definition
# key : value

# Data = {key:value, 
#         key2:value2,
#         key3:value3
# }

# nilai = {
#           "andi" : 80,
#           "andre" : 85,
#           "Beni" : 90,
#           "Bondan" : 75,
#           "joko": 76
# }

## akses data
# print(nilai["andre"])
# print(nilai["Beni"])

# print(nilai.keys()) # memprint nama "andi", "andre," "Beni", 

# print(nilai.values()) 

# # print(nilai['joni']) # error karena joni tidak ada di dalam "nilai"

# print(nilai.get('andre', "Data Tidak Ada"))

# print(nilai.get("joni", "Data Tidak Ada")) # Tidak terjadi apa2 karena joni tidak ada

# add data - create
# nilai["joni"] = 84

# print(nilai.get("joni", "Data Tidak Ada")) 

# ## Update data
# nilai["Beni"] = 95

# nilai.update({"Bondan" : 90})

# print(nilai["Beni"])
# print(nilai["Bondan"])

# ## Hapus Data (Delete)
# nilai.pop("joni")

# # print(nilai["joni"]) # error karena joni sudah dihapus

# ## Read data

# print(nilai) 
# print(nilai.items()) # memprint nama variabel beserta nilainya

# daftarNilai = list(nilai.values()) # memprint nilai dari "nilai" dalam bentuk list
# print(daftarNilai) 

# for i in nilai:
#     print(i)

# for i in nilai.values():
#     print(i)

# nama = input("Masukkan nama yang anda cari: ")

# print(f"Nilai dari nama : {nama} adalah {nilai.get(nama, 'data tidak ada')}")

hari = {
    "senin" : "monday",
    "selasa" : "tuesday",
    "rabu" : "wednesday",
    "kamis" : "thursday",
    "jum'at" : "friday",
    "sabtu" : "saturday",
    "minggu" : "sunday", 
}

# # akses keys based on values

# # dengan cara list
# indo = list(hari.keys()) # pakai list agar didapat indexnya
# eng = list(hari.values())
# print(indo)
# print(eng)

# # dengan cara for
# for i in hari.items():
#     print(i) # i akan dipetakan ke dua nilai keys dan values dari hari
#     print(type(i))

for i, j in hari.items():
    print(i) # i akan dipetakan ke nilai keys dari hari
    print(j) # j akan dipetakan ke nilai values dari hari
    # days == j, hari == i
    # print(type(i))
    # print(type(j))

# packing, unpacking

data = ("andi", 25, "bandung") # packing

# unpacking 
# print(len(data))
nama, usia, kota = data # memetakan nilai "data" ke variabel
print(nama)
print(usia)
print(kota)

a = b = c = 15
print(a)
print(b)
print(c)

a, b, c = 15, "satu", "asti"
# a = 15
# b = "satu"
# c = "asti"
# print(a)
# print(b)
# print(c)

a = 15, "satu", "asti"
print(type(a))

# namaHari = input("Masukkan nama hari (IDN) : ")

# print(f"Nama hari {namaHari} dalam bahasa Inggris adalah {hari[namaHari]}")

# input : 
# - User dapat memasukkan format huruf beda-beda kapital namun tetap OK, SABTU, Sabtu
# - pilihan translate 1. IDN - ENG, 2. ENG - IDN :
# Pilih 1:
# - Silakan masukkan nama hari
# Kondisi : Nama hari yang anda masukkan salah
# Output nya : Nama hari ... dalam bahasa Inggris adalah ...
# Pilih 2:
# - Please input the name of the day 
# Kondisinya : The day that you are looking for is wrong
# Output : Day ... in bahasa is ...

## Format Dict
## CRUD

# member1 = {
#     "name" : "Andre",
#     "age" : 25,
#     "is_married" : False,
#     "job" : "Data Analyst",
#     "cars" : ["Alphard", "Xpander", "Innova"],
#     "address": {
#         "street" : "East Pegangsaan",
#         "RT" : 6,
#         "RW" : 4,
#         "City" : ["East Jakarta", "west jakarta", "south jakarta"],
#         "Zipcode" : 56895,
#         "geo" : {
#             "lat" : 568.632,
#             "lng" : [89.546, 96.65, 45.67]
#             }
#         }
#     }

# member2 = {
#     "name" : "Joni",
#     "age" : 25,
#     "is_married" : False,
#     "job" : "Data Analyst",
#     "cars" : ["Alphard", "Xpander", "Innova"],
#     "address": {
#         "street" : "East Pegangsaan",
#         "RT" : 6,
#         "RW" : 4,
#         "City" : ["East Jakarta", "west jakarta", "south jakarta"],
#         "Zipcode" : 56895,
#         "geo" : {
#             "lat" : 568.632,
#             "lng" : [89.546, 96.65, 45.67]
#             }
#         }
#     }
# login = {101 : 8957464, 102 : "jkl568"}
# # if passuser == login[iduser]: # kalau benar, user dapat masuk. kalau salah, dapat notif password salah

# DataAnggota = {101:member1, 102:member2}

# print(member1["name"])
# print(member1["is_married"])

# print(member1["cars"][1]) # untuk akses list, perlu menyertakan index dari list
# print(member1["address"]["City"][2])

# print(member1["address"]["geo"]["lng"][2])

# member1["salary"] = 15000000
# print(member1["salary"])

# # print(DataAnggota[102]) # semua data pada member2 akan diprint

# print(DataAnggota[102]["address"]["geo"]["lng"][1])