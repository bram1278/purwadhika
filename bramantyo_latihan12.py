# berapa jumlah total dari bilangan ganjil yang telah dipangkat 3 dari 1 - 200

from functools import reduce

# i = []

# for a in range(1,201): # mengisi list i dengan nilai 1 - 200
#     i.append(a)

# pangkat3 = lambda x: x ** 3



# j = list(filter(lambda x: x%2 != 0, a))

## alternatif mas Rifqi
b = list(range(1,201))
odd = list(filter(lambda x: x%2 != 0, b))
pangkat = list(map(lambda x: x ** 3, odd))
jumlah = sum(pangkat)
# print(jumlah)

# jumlah1 = sum(list(map(lambda x: x ** 3, list(filter(lambda x: x%2 != 0, list(range(1,201)))))))

# print(jumnlah1)

## alternatif mbah citra

total = reduce(lambda x,y: x + y, list(map(lambda x: x ** 3, list(range(1,201,2)))))
# print(total)

## alternatif mas Iqbal

hasil = reduce(lambda x,y: x+y, list(map(lambda x: x**3, list(filter(lambda x: x%2 != 0, range(1,201))))))
print(hasil)

