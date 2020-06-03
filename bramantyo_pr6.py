### Personal Assignment
# Latihan 1:

# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

a = ""

for i in range(1,6): 
    
    for j in range(1,i+1):
        a += "{} ".format(i)
    a += "\n"
        
print(a)

print("perintah di luar looping \n")

# Latihan 2:

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

a = ""

for i in range(5): 
   
   for j in range(0,i+1):
       a += "{} ".format(j+1)        
   a += "\n"

print(a)

print("perintah di luar looping \n")

# Latihan 3:

# 5
# 5 4
# 5 4 3
# 5 4 3 2
# 5 4 3 2 1

a = ""

for i in range(5,0,-1): 
   
   for j in range(6,i,-1):
       a += "{} ".format(j-1)        
   a += "\n"

print(a)

print("perintah di luar looping \n")

# Latihan 4:

# 1 1 1 1 1
# 2 2 2 2
# 3 3 3
# 4 4
# 5

a = ""

for i in range(1,6): 
   
   for j in range(6,i,-1):
       a += "{} ".format(i)        
   a += "\n"

print(a)

print("perintah di luar looping \n")

# Latihan 5:
# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1

a = ""

for i in range(5,0,-1): 
   
   for j in range(0,i):
       a += "{} ".format(j+1)        
   a += "\n"

print(a)

print("perintah di luar looping \n")

# Latihan 6:
# 5 4 3 2 1
# 5 4 3 2
# 5 4 3
# 5 4
# 5

a = ""

for i in range(0,5): 
   
   for j in range(6,i+1,-1):
       a += "{} ".format(j-1)        
   a += "\n"

print(a)

print("perintah di luar looping \n")

# Latihan 7:
#         *
#       * * *
#     * * * * * 
#   * * * * * * *
# * * * * * * * * *
# * * * * * * * * *
#   * * * * * * *
#     * * * * *
#       * * * 
#         *

a =''

for i in range (10):
    for j in range (9):
        if abs(i-4) == j and i<5 :
            a += ' * '*(2*i+1)
        elif (i-5) == j and i>=5 :
            a += ' * '*(2*abs(i-9)+1)            
        else :
            a += '   '
    a += '\n'
print(a)


print("perintah di luar looping \n")
# Kirim email: khumaeni@purwadhika.com