# Joni memiliki peternakan, dia beternak kambing dan ayam, jumlah nya 13, jumlah kaki nya 32
# berapa jumlah ayam dan berapa jumlah kambing?

# print("jumlahkambing = x")
# print("jumlahayam = y")
# print ("x+y = 13, y = 13 - x")
# print ("Jumlah kaki x = 4")
# print ("Jumlah kaki y = 2")
# print ("4*x + (y*2 = 32")
# print (4*x = 32 - 2*y)
# print (kakikambing*jumlahkambing = jumlahkaki - kakiayam*jumlahayam)
# print (jumlahkambing = (jumlahkaki - kakiayam*jumlahayam)/kakikambing)

# print ("2*x + 26 = 32")
# print ("2*x = 6")
# print ("x = 3")
# print ("y = 13 - 3")
# print ("y = 10")

JumlahTotal = 13
JumlahKaki = 32
KakiAyam = 2
KakiKambing = 4

Kambing = abs((KakiAyam * JumlahTotal - JumlahKaki)/(KakiKambing-KakiAyam))
Ayam = JumlahTotal - Kambing

print(f"Jumlah kambing adalah {Kambing}, Jumlah ayam adalah {Ayam}")