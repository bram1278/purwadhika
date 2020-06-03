# buah = ["mangga", "jeruk", "apel", "alpukat"]
# kombinasi = ["susu", "keju", "coklat", "apel", "mangga"]
# gunakan list comprehension
# (mangga,susu), (mangga, keju), (mangga, coklat) ..... tapi tak ada yg sama
# (mangga, mangga) tak ada
# (apel, apel) tak ada
###############################################

buah = ["mangga", "jeruk", "apel", "alpukat"]
kombinasi = ["susu", "keju", "coklat", "apel", "mangga"]
kombo = []
# buah1 = set(buah)
# kombinasi1 = set(kombinasi)

# for i in range(0,len(buah)):
#     for j in range(0,len(kombinasi)):
#         if kombinasi[j] not in buah[i]:
#             kombo = kombo + [buah[i],kombinasi[j]]
#         else:
#             pass
# print(kombo)

new = [(i,j) for i in buah for j in kombinasi if i != j]
print(new)