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

# Kalau bisa pembuatan himpunan menggunakan fungsi

A = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
B = {1, 3, 5, 7, 9, 11, 13, 15, 17, 19}
C = {-19, -18, -17, -16, -15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1}
D = {2, 3, 5, 7, 11, 13, 17, 19}
E = {4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20}

# a. A ∪ B ∪ C ∪ D ∪ E

print(A | B | C | D | E)

# b. (A ∩ B) ∪ (D ∩ E)

print((A & B) | (D & E))

#c. (A ∪ B) ∩ (D ∪ E)

print((A | B) & (D | E))

#d. (A ∪ B) - (D ∪ E)

print((A | B) - (D | E))

#e. (A ∪ B ∪ C) - (A ∩ E)

print((A | B | C) - (A & E))