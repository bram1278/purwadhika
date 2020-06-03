password = "rahasia"
cek = ''
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
            break
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

opsiuser = int(input('please press [1/2/3/4/5]: '))
fruits = ['apple','banana','pear','cherry','kiwi','oranges']
vegetables = ['cucumber','kale','cauliflower','broccoli','spinach']
instants = ['corned beef','instant noodle','chicken nugget','canned sardines','spam']
check = ' '
opsi1 = 1
opsi4 = 4

while check != opsiuser:
    if opsiuser == 1:
        print('=== SHOW LOG ===')
        print('fruits:',fruits)
        if fruits == []:
            print('The fruits list is empty')
        print('vegetables:', vegetables)
        if vegetables == []:
            print('The vegetables list is empty')
        print('instants:', instants)
        if instants == []:
            print('The instants list is empty')
        break
    elif opsiuser == 2:
        print('=== CREATE LOG ===')
        var = input('fruits/vegetables/instants:')
        if var == 'fruits':
            edit = input('please input the item that you want to remove:')
            editx = edit.lower()
            i = len(fruits)
            for n in range(0,i+1):
                if n == i:
                    fruits.discard(editx)
                    print('The data that you input already deleted')
                    print('fruits:',fruits)
                    break
                elif editx == fruits[n]:
                    delete = str(input('The list already contained the data that you input, do you want to add it? (Y/N)'))
                    delete2 = delete.lower()
                    if create2 == 'y':
                        fruits.append(editx)
                        print('The data that you input is saved')
                        print('fruits:',fruits)
                        break
                    elif create2 == 'n':
                        print('The data that you input is not saved')
                        print('fruits:',fruits)
                        break
                    else:
                        print('The input is wrong, please try again')
                        continue
        elif var == 'vegetables':
            edit = input('please input item you want to change:')
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
        elif var == 'instants':
            edit = input('please input item you want to remove:')
            editx = edit.lower()
            i = len(instants)
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
        else:
            print('none in log')

    elif opsiuser == 3:
        print('=== REMOVE LOG ===')
        var = input('fruits/vegetables/instants:')
        if var == 'fruits':
            rmv = input('please input item you want to remove:').lower()
            rmv1 = fruits.remove(rmv)
            print(rmv1)
            print(fruits)
        elif var == 'vegetables':
            rmv = input('please input item you want to remove:').lower()
            rmv1 = vegetables.remove(rmv)
            print(rmv1)
            print(vegetables)
        elif var == 'instants':
            rmv = input('please input item you want to remove:').lower()
            rmv1 = instants.remove(rmv)
            print(rmv1)
            print(instants)
    elif opsiuser == 4:
        print('=== UPDATE LOG ===')
        var = input('fruits/vegetables/instants:')
        if var == 'fruits':
            upd = input('please input item that you want to change/update:').lower()
            upd1 = input('please input the new name for the item:').lower()
            var1 = fruits.index(upd)
            fruits[var1] = upd2
            print(fruits)
        if var == 'vegetables':
            upd = input('please input item that you want to change/update:').lower()
            upd1 = input('please input the new name for the item:').lower()
            var1 = vegetables.index(upd)
            vegetables[var1] = upd2
            print(vegetables)
        if var == 'instans':
            upd = input('please input item that you want to change/update:').lower()
            upd1 = input('please input the new name for the item:').lower()
            var1 = instants.index(upd)
            instants[var1] = upd2
            print(instants)
        
    elif opsiuser == 5:
            print('=== EXIT ===')
            break
    else:
        print('Your input is wrong, please input a number from 1 to 5')


