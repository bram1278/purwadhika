# Latihan:
# input : masukan kalimat

# outputnya : kata dalam kalimat dibalik

# misalnya, input : "nama saya joni"
# outputnya: "aman ayas inoj"

kalimat = str(input("Masukkan kalimat anda: ")) # kalimat adalah variabel input string

kata = kalimat.split(" ") # input kalimat dipecah dalam bentuk tuple
a = len(kata) # variabel a adalah total jumlah isi tuple dari variabel kata

hurufbalik = '' # variabel hurufbalik diset ke string kosong

for balikkata in range(0,a): # mengecek apakah variabel balikkata (integer) sudah mencapai jumlah kata dari input kalimat
    huruf = str(kata[balikkata]) # tuple kata diubah menjadi format string
    b = len(huruf) # menghitung total jumlah karakter dari huruf yang sedang diperiksa pada pengulangan saat ini
    
    for balikhuruf in range(0,b): # mengecek apakah variabel balikhuruf (integer) sudah mencapai jumlah huruf dari kata yang diperiksa saat ini
        hurufbalik = hurufbalik + huruf[b - 1 - balikhuruf] # formula untuk membalikkan urutan huruf
        
        if balikhuruf == (b - 1): # mengecek apakah variabel balikhuruf (integer) bernilai sama dengan b - 1
            hurufbalik = hurufbalik + ' ' # spasi dimasukkan ke variabel hurufbalik
    
print(hurufbalik) # memprint variabel hurufbalik