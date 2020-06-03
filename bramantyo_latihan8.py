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

hari = {
    "senin" : "monday",
    "selasa" : "tuesday",
    "rabu" : "wednesday",
    "kamis" : "thursday",
    "jum'at" : "friday",
    "sabtu" : "saturday",
    "minggu" : "sunday",
}

translasi = {"Silakan input pilihan translasi / Please insert your translation option \n (1. IDN - ENG) (2. ENG - IDN): "} # translasi adalah variabel input 

hari1 = list(hari)
day = list(hari.values())

while(True):
    for i in translasi:
        print(i)
    pilihan = int(input("Masukkan input anda / Please insert your input : ")) # pilihan adalah variabel input integer
    if pilihan == 1:
        indo = input("Masukkan nama hari: ")
        indo1 = indo.lower()  
        if (indo1 in hari1):
            eng = day[hari1.index(indo1)]
            print(f"Nama hari {indo1} dalam bahasa Inggris adalah {eng}")
        else:
            print("Nama hari yang anda masukkan salah \n Catatan: Gunakan hari jum'at atau Jum'at, bukan jumat atau Jumat")
    elif pilihan == 2:
        eng = input("Please input the name of day: ") # eng adalah variabel input 
        eng1 = eng.lower()
        if (eng1 in day):
            indo = hari1[day.index(eng1)]
            print(f"Day {eng1} in bahasa is {indo}")
        else :
            print("The day that you input is wrong")
    else:
        print("Terima kasih / Thank you")
        break