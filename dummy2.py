# Lat 4: 
# pakai def: 
# Caesar cipher
# masukkan kata : Joni
# masukkan angka : 2
# hasil caesar cipher : Lnpk (huruf maju dua)

# masukkan kata : Joni
# masukkan angka : -2
# hasil caesar cipher : hmlg  (huruf mundur dua)

alfabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] # list berisi urutan alfabet

kata = input('Silahkan masukkan kata (jangan masukkan angka, spasi, atau tanda simbol lainnya): ')
angka = int(input('Silahkan masukkan angka (bisa bertanda plus atau minus): '))

kecil = kata.lower() # agar input user tidak case sensitive
katabaru = ''

batas = len(alfabet) # bernilai 26, konstanta bertipe int yang menjadi penentu kondisi if agar operasi pergeseran alfabet tidak keluar dari rentang index yang diizinkan

if kecil.isalpha() : # mengecek apakah input user adalah alfabet saja (True) atau tidak (False)
    cek = list(kecil) # mengubah input kata menjadi list yang isinya masing-masing alfabet
    for a in range(0,len(cek)):
        cek1 = alfabet.index(cek[a]) # perintah index untuk mengecek urutan ke-berapakah input user pada daftar alfabet; tidak bisa dijalankan untuk objek set sehingga digunakan list 
        if cek1 + angka <= (batas - 1):
            katabaru = katabaru + alfabet[cek1 + angka] # katabaru adalah kata dari alfabet yang urutannya telah dijumlahkan/dikurangi dengan input angka, cek1 bertipe int
        elif cek1 + angka > (batas - 1): # jika hasil penjumlahan cek1 dan angka di atas alfabet ke-26 (z), cth: z dinaikkan sebesar 1 akan berubah menjadi a
            katabaru = katabaru + alfabet[cek1 + angka%26 - (batas)]
        elif cek1 + angka < 0: # jika hasil pengurangan cek1 dan angka di bawah alfabet pertama (a), cth: a diturunkan sebesar 1 akan berubah menjadi z
            katabaru = katabaru + alfabet[cek1 + angka%26 + (batas)]
    print(f"Kata yang baru menjadi ",katabaru)
else: 
    print("Inputan anda salah")