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
    print(f"Nama hari {translasi1} dalam bahasa Inggris adalah {eng1}")
elif translasi1 in day:
    indo = lambda i, j, k: i[j.index(k)]
    indo1 = indo(hari,day,translasi1) 
    print(f"Day {translasi1} in bahasa is {indo1}")
else:
    print("Input anda tidak terdeteksi / Your input is not detected \n Catatan: Gunakan hari jum'at atau Jum'at, bukan jumat atau Jumat")    