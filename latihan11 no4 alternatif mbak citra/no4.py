# Lat 4:
# Buat def atau function 
# ada deret angka
# 1 2 3 4 5
# 6 7 8 9
# 11 12 13 14 15
# 16 17 18 19 20
# 21 22 23 24 25
# input: spin ke: pilihan ke 1-4
# pilihan 1:
# 21 16 11 6 1
# 22 17 12 7 2
# 23 18 13 8 3
# 24 19 14 9 4
# 25 20 15 10 5

# pilihan 2:
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

# pilihan 4:
# 1 2 3 4 5
# 6 7 8 9 10
# 11 12 13 14 15
# 16 17 18 19 20
# 21 22 23 24 25

def rotasi(x):
    z = ''

    if x == 1:
        for i in range(21, 26):
            for j in range(0, 25, 5):
                z += str(i - j) + ' '
            z += '\n'

    elif x == 2:
        for i in range(25, 0, -5):
            # if i >= 5:
            for j in range(i + 1, i - 4, -1):
                z += str(j - 1) + ' '
            z += '\n'

    elif x == 3:
        for i in range(6, 1, -1):
            for j in range(0, 5):
                z += str(i - 1 + (5 * j)) + ' '
            z += '\n'

    elif x == 4:
        for i in range(0, 25, 5):
            for j in range(i, i + 5):
                z += str(j + 1) + ' '
            z += '\n'

    return f"Pilihan {x}\n{z}"


print(rotasi(1))
print()
print(rotasi(2))
print()
print(rotasi(3))
print()
print(rotasi(4))