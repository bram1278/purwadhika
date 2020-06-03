password = "rahasia" # mengeset variabel password
cek = '' # mengeset variabel input
passenter = 1 
maxenter = 5

while cek != password:
    if passenter <= maxenter:
        cek = input('enter password: ')
        if cek != password and passenter < 5:
            passenter += 1
            print('percobaan ke ', passenter, ', salah. coba lagi')
        elif cek != password and passenter ==5:
            passenter += 1
            print('try again later')
            exit
        else:
            print("loggin in")

print('='*50)
print('welcome to StockLog app ver.0.0.1')
print('='*50)
print('===== MENU =====')
print('[1] SHOW LOG')
print('[2] CREATE LOG')
print('[3] REMOVE LOG')
print('[4] UPDATE LOG')
print('[5] EXIT')

fruits = ['apple','banana','pear','cherry','kiwi','oranges']
vegetables = ['cucumber','kale','cauliflower','broccoli','spinach']
instants = ['corned beef','instant noodle','chicken nugget','canned sardines','spam']
check = 5
opsiuser = 1

while check != opsiuser:
    opsiuser = int(input('please press [1/2/3/4/5]: '))
    if opsiuser == 1:
        print('=== SHOW LOG ===')
        print('fruits: ',fruits) 
        if fruits == []: # jika isi list dari fruits kosong
            print('The fruits list is empty') 
        print('vegetables: ', vegetables) 
        if vegetables == []: # jika isi list dari vegetables kosong 
            print('The vegetables list is empty')
        print('instants:', instants)
        if instants == []: # jika isi list dari instants kosong 
            print('The instants list is empty')

    elif opsiuser == 2: # jika user memilih opsi untuk menambahkan data baru ke sebuah list
        print('=== CREATE LOG ===')
        var = input('fruits/vegetables/instants:') # user memilih input list mana yang akan ditambahkan data baru
        if var == 'fruits':
            edit = input('please input item that you want to add:') # mengeset variabel input bernama edit
            editx = edit.lower() # variabel input edit yang di-lowercase
            i = len(fruits) # menghitung berapa banyak isi list fruits
            for n in range(0,i+1): # mengeset looping for dengan variabel n sebagai variabel penentu dan batasnya ditentukan variabel i
                if n == i: # jika n telah bernilai sama dengan i
                    fruits.append(editx) # variabel editx (input user yang di-lowercase) ditambahkan ke list yang ditangani pada pengulangan ini
                    print('The data that you input is saved') # memprint tanda notif bahwa input user berhasil ditambahkan ke list
                    print('fruits:',fruits) # memprint list yang baru
                    break # mengakhi for looping
                elif editx == fruits[n]: # jika editx bernilai sama dengan isi index dari list yang dicari pada pengulangan ini
                    create = str(input('The list already contained the data that you input, do you want to add it? (Y/N)')) # buat variabel input create yang menentukan apakah user tetap ingin menambahkan atau tidak
                    create2 = create.lower() # variabel input create yang di-lowercase bernama create2
                    if create2 == 'y': # jika user menginput 'y' atau 'Y'
                        fruits.append(editx) # variabel editx (input user yang di-lowercase) ditambahkan ke list yang ditangani pada pengulangan ini
                        print('The data that you input is saved') # memprint tanda notif bahwa input user berhasil ditambahkan ke list
                        print('fruits:',fruits) # memprint list yang baru
                        break # mengakhiri for looping
                    elif create2 == 'n': # jika user menginput 'n' atau 'N'
                        print('The data that you input is not saved') # memprint tanda notif bahwa input user tidak ditambahkan ke list
                        print('fruits:',fruits) # memprint list yang tidak ditambahkan masukan user
                        break # mengakhiri for looping
                    else: # jika input user tidak sama dengan 'y', 'Y', 'n', atau 'N'
                        print('The input is wrong, please try again') # memprint tanda notif bahwa input user salah
                        break # mengakhiri for looping
        elif var == 'vegetables': # sama dengan kode untuk fruits, tetapi variabel fruits diganti menjadi vegetables
            edit = input('please input item you want to add:')
            editx = edit.lower()
            i = len(vegetables)
            for n in range(0,i+1):
                if n == i:
                    vegetables.append(editx)
                    print('The data that you input is saved')
                    print('vegetables:',vegetables)
                    break
                elif editx == vegetables[n]:
                    create = str(input('The list already contained the data that you input, do you want to add it? (Y/N)'))
                    create2 = create.lower()
                    if create2 == 'y':
                        vegetables.append(editx)
                        print('The data that you input is saved')
                        print('vegetables:',vegetables)
                        break
                    elif create2 == 'n':
                        print('The data that you input is not saved')
                        print('vegetables:',vegetables)
                        break
                    else:
                        print('The input is wrong, please try again')
                        break
        elif var == 'instants': # sama dengan kode untuk fruits, tetapi variabel fruits diganti menjadi instants
            edit = input('please input item you want to add:')  # mengeset variabel input bernama edit
            editx = edit.lower() # variabel input edit yang di-lowercase
            i = len(instants) # menghitung berapa banyak isi list fruits
            for n in range(0,i+1):
                if n == i:
                    instants.append(editx)
                    print('The data that you input is saved')
                    print('instants:',instants)
                    break
                elif editx == instants[n]:
                    create = str(input('The list already contained the data that you input, do you want to add it? (Y/N)'))
                    create2 = create.lower()
                    if create2 == 'y':
                        instants.append(editx)
                        print('The data that you input is saved')
                        print('instants:',instants)
                        break
                    elif create2 == 'n':
                        print('The data that you input is not saved')
                        print('instants:',instants)
                        break
                    else:
                        print('The input is wrong, please try again')
                        break
        else: # jika input user bukan fruits, vegetables, atau instants
            print('none in log')

    elif opsiuser == 3: # opsi untuk menghapus isi list berdasarkan input user
        print('=== REMOVE LOG ===')
        var = input('fruits/vegetables/instants:') # user memasukkan input list mana yang isinya akan dihapus
        if var == 'fruits':
            i = len(fruits) # menghitung total jumlah isi list
            j = i - 1 # mengeset variabel
            k = j # mengeset variabel
            n = 0 # mengeset variabel
            edit = input('please input the item that you want to remove: ') # input yang dimasukkan user
            editx = edit.lower() # input user yang dibuat menjadi lowercase seandainya user memasukkan huruf kapital/besar

            while n <= j: # while digunakan karena variabel pembatas loop dapat disesuaikan dengan kebutuhan, berbeda dengan for ... in ... yang pembatas loopnya fixed
                if editx == fruits[n]: # mengecek apakah input user ada di index dalam daftar
                    fruits.remove(editx) # jika kondisi terpenuhi, isi index dalam daftar tersebut dihapus
                    j -= 1 # nilai j digeser karena setelah command remove, ada pergeseran index yang berkurang sebesar 1, misal: daftar[0] yang baru berasal dari daftar[1] sebelumnya, dst
                    n = 0 # untuk mengulang proses looping, nilai n diset 0 agar pengecekan dimulai dari daftar[0] yang baru
                elif n == j and j == k: # mengecek apakah nilai n sudah sama dengan j dan apakah nilai j ada perubahan atau tidak
                    print('The data that you input does not exist in the list') # jika kondisi memenuhi, berarti tidak ada perubahan daftar; dengan kata lain, input tidak eksis di daftar
                    break # proses looping diakhiri 
                else: # jika tidak ada data yang dihapus, variabel n bertambah 1 (n = n + 1)
                    n += 1 
            print('fruits:',fruits)       

        elif var == 'vegetables':
            i = len(vegetables) # menghitung total jumlah isi list
            j = i - 1 # mengeset variabel
            k = j # mengeset variabel
            n = 0 # mengeset variabel
            edit = input('please input the item that you want to remove: ') # input yang dimasukkan user
            editx = edit.lower() # input user yang dibuat menjadi lowercase seandainya user memasukkan huruf kapital/besar

            while n <= j: # while digunakan karena variabel pembatas loop dapat disesuaikan dengan kebutuhan, berbeda dengan for ... in ... yang pembatas loopnya fixed
                if editx == vegetables[n]: # mengecek apakah input user ada di index dalam daftar
                    vegetables.remove(editx) # jika kondisi terpenuhi, isi index dalam daftar tersebut dihapus
                    j -= 1 # nilai j digeser karena setelah command remove, ada pergeseran index yang berkurang sebesar 1, misal: daftar[0] yang baru berasal dari daftar[1] sebelumnya, dst
                    n = 0 # untuk mengulang proses looping, nilai n diset 0 agar pengecekan dimulai dari daftar[0] yang baru
                elif n == j and j == k: # mengecek apakah nilai n sudah sama dengan j dan apakah nilai j ada perubahan atau tidak
                    print('The data that you input does not exist in the list') # jika kondisi memenuhi, berarti tidak ada perubahan daftar; dengan kata lain, input tidak eksis di daftar
                    break # proses looping diakhiri 
                else: # jika tidak ada data yang dihapus, variabel n bertambah 1 (n = n + 1)
                    n += 1 
            print('vegetables: ',vegetables)

        elif var == 'instants':
            i = len(instants) # menghitung berapa banyak isi list
            j = i - 1 # mengeset variabel
            k = j # mengeset variabel
            n = 0 # mengeset variabel
            edit = input('please input the item that you want to remove: ') # input yang dimasukkan user
            editx = edit.lower() # input user yang dibuat menjadi lowercase seandainya user memasukkan huruf kapital/besar

            while n <= j: # while digunakan karena variabel pembatas loop dapat disesuaikan dengan kebutuhan, berbeda dengan for ... in ... yang pembatas loopnya fixed
                if editx == instants[n]: # mengecek apakah input user ada di index dalam daftar
                    instants.remove(editx) # jika kondisi terpenuhi, isi index dalam daftar tersebut dihapus
                    j -= 1 # nilai j digeser karena setelah command remove, ada pergeseran index yang berkurang sebesar 1, misal: daftar[0] yang baru berasal dari daftar[1] sebelumnya, dst
                    n = 0 # untuk mengulang proses looping, nilai n diset 0 agar pengecekan dimulai dari daftar[0] yang baru
                elif n == j and j == k: # mengecek apakah nilai n sudah sama dengan j dan apakah nilai j ada perubahan atau tidak
                    print('The data that you input does not exist in the list') # jika kondisi memenuhi, berarti tidak ada perubahan daftar; dengan kata lain, input tidak eksis di daftar
                    break # proses looping diakhiri 
                else: # jika tidak ada data yang dihapus, variabel n bertambah 1 (n = n + 1)
                    n += 1 
            print('instants: ',instants)
        else: # jika input user bukan fruits, vegetables, atau instants
            print('none in log')

    elif opsiuser == 4: # jika user memilih input untuk opsi mengupdate/mengubah isi list
        print('=== UPDATE LOG ===')
        var = input('fruits/vegetables/instants: ') # user memasukkan input list mana yang isinya akan diubah
        if var == 'fruits': # jika user memilih list fruits
            upd = input('please input item that you want to change/update: ').lower() # user memasukkan nama dari list fruits yang akan digantikan
            upd1 = input('please input the new name for the item: ').lower() # user memasukkan nama baru yang akan menggantikan isi list lama
            i = len(fruits) # menghitung berapa banyak isi list
            for n in range(0,i+1): # mengeset looping for dengan variabel n sebagai variabel penentu dan batasnya ditentukan variabel i
                if n == i: # jika n telah bernilai sama dengan i
                    print('The data that you input does not exist in the list') # memprint notif bahwa input nama lama yang akan digantikan tidak ada di dalam daftar list
                    break # mengakhiri looping for
                elif upd == fruits[n]: # jika input yang dimasukkan user adalah sama dengan isi index dari list yang diperiksa pada pengulangan ini
                    fruits[n] = upd1 # isi index dari list akan diubah menjadi nama yang baru
                    break # mengakhiri looping for
            print('fruits: ',fruits)    
        
        elif var == 'vegetables': # sama dengan kode untuk fruits, tetapi variabel fruits diganti menjadi vegetables
            upd = input('please input item that you want to change/update: ').lower()
            upd1 = input('please input the new name for the item: ').lower()
            i = len(vegetables)
            for n in range(0,i+1):
                if n == i:
                    print('The data that you input does not exist in the list')
                    break
                elif upd == vegetables[n]:
                    vegetables[n] = upd1
                    break
            print('vegetables: ',vegetables)  
        elif var == 'instants': # sama dengan kode untuk fruits, tetapi variabel fruits diganti menjadi instants
            upd = input('please input item that you want to change/update: ').lower()
            upd1 = input('please input the new name for the item: ').lower()
            i = len(instants)
            for n in range(0,i+1):
                if n == i:
                    print('The data that you input does not exist in the list')
                    break
                elif upd == instants[n]:
                    instants[n] = upd1
                    break
            print('instants: ',instants)
        else: # jika input user bukan fruits, vegetables, atau instants
            print('none in log')
        
    elif opsiuser == 5: # jika user memilih opsi untuk exit
            print('=== EXIT ===')
            break
    else: # jika user memilih input selain 1 - 5
        print('Your input is wrong, please input a number from 1 to 5')


