# Latihan:
# A = himpunan bilangan genap dari 1 -20
# B = himpunan bilangan ganjil dari 1 -20
# C = himpunan bilangan negatif lebih dari -20
# D = himpunan Bilangan prima dari 1 - 20
# E = himpunan bilangan komposit dari 1 - 20

# Bilangan komposit = Bukan Bilangan prima

# Output :

# a. A ∪ B ∪ C ∪ D ∪ E

# b. (A ∩ B) ∪ (D ∩ E)

# c. (A ∪ B) ∩ (D ∪ E)

# d. (A ∪ B) - (D ∪ E)

# e. (A ∪ B ∪ C) - (A ∩ E)

# menggunakan fungsi set(range(x,y,z)) ---> menampilkan range angka dengan cara memasukan tiga argumen yaitu : batas bawah (x) , batas atas (y), dan steps (z)
# | = union , & = intersection , - = difference.

# A = (set(range(2,21,2)))
# B = (set(range(1,20,2)))
# C = (set(range(-19,0)))
# D = {2,3,5,7,11,13,17,19}
# E = {4,6,8,9,10,12,14,15,16,18}

# print(A)
# print(B)
# print(C)
# print(D)
# print(E)

# a = (A | B | C | D | E)
# b = ((A & B) | (D & E))
# c = ((A|B) & (D|E))
# d = ((A|B) - (D|E))
# e = ((A|B|C) - (A&E))

# print(a)
# print(b)
# print(c)
# print(d)         
# print(e)

# #trial untuk prime number
A = []
for num in range(2,21,2):
    A.append(num)

print(A)

B = [] 
for num1 in range(1,20,2):
    B.append(num1)

print(B)

C = []
for num2 in range (-19,0):
    C.append(num2)

print(C)

D = []
for num3 in range(2,20):  
   if num3 > 1:  
       for i in range(2,num3):  
           if (num3 % i) == 0:  
               break  
       else:  
           D.append(num3)

print(D)


E = []
for num4 in range(2,20):
    for j in range(2,num4):
            if (num4 % j ) == 0:
                E.append(num4)
                break

print(E)

F = [A,B]

print(F)

# z = ''

# for item in range(5,0,1):
#     for item1 in range(5):
#         z += item1
#     z += item

# print(z)
              
