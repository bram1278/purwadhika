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

print('welcome to StockLog app ver.0.0.1')
opsiuser = int(input('press 1 for entry, press 2 to read log, press 3 to edit:   '))
fruits = ['apple','banana','pear','cherry','kiwi','oranges']
vegetables = ['cucumber','kale','cauliflower','broccoli','spinach']
instants = ['corned beef','instant noodle','chicken nugget','canned sardines','spam']
if (opsiuser == 1):
    print('README: to enter data, please enter 1 for fruits, 2 for vegetables, 3 for instant foods. press 9 to go back to the previous menu') 
#di bawah sini akan ada int(input), diikuti if/elif/else, untuk mudah mengakses data hanya dengan input angka 1, 2, 3, 9
elif (opsiuser == 2):
    print('your current stock:')
    print([fruits,vegetables,instants])
#hanya fungsi print untuk melihat stock
elif (opsiuser == 3):
    print('README: to delete data, please enter 1 for fruits, 2 for vegetables, 3 for instant foods. press 9 to go back to the previous menu')
#di bawah sini akan ada int(input), diikuti if/elif/else, untuk mudah mengakses data hanya dengan input angka 1, 2, 3, 9
else:
    print('please enter the correct command')
