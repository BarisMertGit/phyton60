# #dictionary


# # sozluk1= {"free": "beleş", "book": "kitap", "computer": "bilgisayar"}
# # print(sozluk1)
# # print(type(sozluk1))

# # sozluk1= {}
# # print(sozluk1)

# # sozluk1 = dict()
# # print(sozluk1)




# #  sozluk1= {"free": "beleş", "book": "kitap", "computer": "bilgisayar"}

# # print(sozluk1["free"])
# # print(sozluk1["book"])
# # print(sozluk1["computer"])
# # print(sozluk1["kitap"])


# # sozluk1= {"free": "beleş", "book": "kitap", "computer": "bilgisayar", "bir" : [1,2,3,4], "iki" : (1,2,3), "uc": {1: "a", 2: "b"}}
# # print(sozluk1["uc"])
# # print(sozluk1["uc"][1])
# # print(sozluk1["bir"])
# # print(sozluk1["bir"][2])

# # sozluk1["iki"][2] += 10
# # print(sozluk1["iki"])




# # sozluk1= {"free": "beleş", "book": "kitap", "computer": "bilgisayar"}
# # sozluk1["pencil"] = "kalem"
# # print(sozluk1)








# sozluk1 = {
#     "sayı1": {"bir": 1, "iki": 2, "üç": 3},
#     "meyveler": {"kış": "portakal", "yaz": "kiraz", "sonbahar":"elma, armut"}
# }

# print(sozluk1)
# print(sozluk1["sayı1"]["bir"])
# print(sozluk1["meyveler"]["kış"])


sozluk = {
    "freedom1": "özgürlük", "fly5": "sinek", "fire2": "alev",
    "freedom2": "özgürlük", "fly4": "sinek", "fire1": "alev",
    "freedom3": "özgürlük", "fly3": "sinek", "fire3": "alev",
    "freedom4": "özgürlük", "fly2": "sinek", "fire4": "alev",
    "freedom5": "özgürlük", "fly1": "sinek", "fire5": "alev",
    }
print(list(sozluk.values()))
print(sozluk.values())
print(sozluk.keys())
print(list(sozluk.keys()))
print(sozluk.items())
print(list(sozluk.items()))