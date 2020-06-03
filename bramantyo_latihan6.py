A = []
for i in range(1,21):
    if i%2==0:
        A.append(i)

print(A)        
    

print("=" * 100) 

B = []
for i in range(1,21):
    if i%2!=0:
        B.append(i)
        
print(B)    

print("=" * 100)    

C = []
for i in range(-19,0):
    C.append(i)

print(C)

print("=" * 100)

D = []
E = []
for i in range(2,21):
    if i==2 or i==3 or (i%2!=0 and i%3!=0):
        D.append(i)
    else:
        E.append(i)
print(D)
print(E)

print("=" * 100)

# atau (cara mas Iqbal Pratama)

D = []
for num3 in range(2,21):  
   if num3 > 1:  
       for i in range(2,num3):  
           if (num3 % i) == 0:  
               break  
       else:  
           D.append(num3)

print(D)


E = []
for num4 in range(2,21):
    for j in range(2,num4):
            if (num4 % j ) == 0:
                E.append(num4)
                break

print(E)

print("=" * 100)

# F = list()
# for i in range(1,21):
#     if i%2 == 0:
#         A.append(i)
#     else:
#         B.append(i)
F=[A,B]

print (F)

print("=" * 100)