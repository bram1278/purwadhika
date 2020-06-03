def romawi():
    rom = {
        'I': 1,
        'IV': 4,
        'V': 5,
        'IX': 9,
        'X': 10,
        'XL': 40,
        'L': 50,
        'XC': 90,
        'C': 100,
        'CD': 400,
        'D': 500, 
        'CM': 900,
        'M': 1000
    }

    loop = True 
    while loop:

        greet = "Translator (Encoder - Decoder Angka Romawi)"
        print(len(greet) * "=")
        print(greet)
        print(len(greet) * "=")
        print("Silakan Pilih Menu:\n1. Angka Romawi --> Nilai\n2. Nilai --> Angka Romawi\n3. Keluar")
        
        try:
            pilihmenu = int(input("Pilihan Menu: "))

            if pilihmenu == 1:
                angka_rom = input("Masukkan Angka Romawi: ")
                rom_key = rom.keys()
                hasil = 0
                temp = []
                for i in angka_rom:
                    if i in rom_key:
                        hasil += rom[i]
                        temp.append(rom[i])

                if len(temp) == len(angka_rom):
                    print(f"Nilai dari angka Romawi {angka_rom} adalah {hasil}.")
                else:
                    print("Angka Romawi yang Anda masukkan salah.")
                lanjut = input("Ingin melanjutkan Romawi Translator (Y/Else)? ").lower()
                if lanjut != 'y':
                    print("Thank you.")
                    loop = False

            elif pilihmenu == 2:
                nilai = int(input("Masukkan Nilai Anda: "))
                if 0 <= nilai <= 4000:
                    new_rom = {v: k for k, v in rom.items()}
                    rom_val = rom.values()
                    romawi_baru = ''
                    sisa = nilai
                    for i in sorted(rom_val, reverse=True):
                        if sisa >= i:
                            sisa_bagi = sisa // i
                            sisa -= (sisa_bagi * i)
                            romawi_baru += sisa_bagi * new_rom[i]
                    print(f"Angka Romawi dari nilai {nilai} adalah {romawi_baru}.")
                    lanjut = input("Ingin melanjutkan Romawi Translator (Y/Else)? ").lower()
                    if lanjut != 'y':
                        print("Thank you.")
                        loop = False
                else:
                    print("Nilai hanya boleh dari rentang 1 - 4000.")
            elif pilihmenu == 3:
                print("Thank you.")
                loop = False
            else:
                print("Pilihan Menu yang Anda masukkan salah.")
                loop = False
        except:
            print("Pilihan Menu yang Anda masukkan salah.")
            loop = False

romawi()