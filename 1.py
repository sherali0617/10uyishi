import os
os.system("cls")
# users = [
#     'Abdulla Abdullaev',
#     'Samandar Asadov',
#     'Shaxnoza Jurayeva',
#     'Ikrom Karimov',
#     'Gulnora Xalilova',
#     'Ziyoda Yuldashova'
# ]

# men = []
# women = []

# for user in users:
#     # Oxirgi 2 ta harfni olamiz
#     oxiri2 = user[-2:] 

#     if oxiri2 == "ov" or oxiri2 == "ev":
#         men.append(user)
#     elif oxiri2 == "va":
#         women.append(user)

# print("Erkaklar:", men)
# print("Ayollar:", women)


# 2.m
# products = {
#     "olma": [13000, 14000, 15000],
#     "anor": [19000, 22000, 24000, 15000],
#     "gilos": [6000, 9000, 5000, 4000],
#     "banan": [30000, 28000]
# }

# for k,q in products.items():
#     ortacha = sum(q) / len(q)
#     print(f"{k}: {int(ortacha)}")


# 3.m
# books = [
#     ("O'tkan kunlar", "Roman"),
#     ("Mehrobdan chayon", "Roman"),
#     ("Shum bola", "Povest"),
#     ("Alkimyogar", "Roman"),
#     ("Boy va kambag'al", "Hikoya"),
#     ("Urush va tinchlik", "Roman"),
#     ("Kecha va kunduz", "Roman"),
#     ("Yulduzli tunlar", "Povest"),
#     ("Qorako'z Majnun", "Hikoya"),
#     ("Qalb ko'zi", "Hikoya")
# ]

# guruhlar={}
# for nomi,janri in books:
#     if janri not in guruhlar:
#         guruhlar[janri]=[]
#     guruhlar[janri].append(nomi)
# print(guruhlar)


# 4.m
# def bank_hisob(depozit,foiz,yil):
#     daromad = (depozit * foiz * yil)/100
#     return depozit + daromad

# print(bank_hisob(10000, 24, 3)) 


