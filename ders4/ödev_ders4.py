
## Kullanıcıdan aldığınız 3 tane sayıyı çarparak ekrana yazdırın. Ekrana yazdırma işlemini ***format*** metoduyla yapmaya çalışın."

# a = int(input("birsayı giriniz: " ))
# b = int(input("ikinci sayıyı girin:" ))
# c = int(input("üçüncü sayınız girin:"))

# print("sayıların çarpımı: ", format(a*b*c))

## "Kullanıcıdan aldığınız **boy** ve **kilo** değerlerine göre kullanıcının beden kitle indeksini bulun.\n"

kilonuz = int(input("kilonuzu giriniz:"))
boyunuz = float(input("boyunuzu giriniz:"))

print("vücüt kitle endeksiniz:", format(int(kilonuz) / (float(boyunuz) ** 2)))



## "Bir aracın kilometrede ne kadar yaktığı ve kaç kilometre yol yaptığı bilgilerini alın ve sürücünü toplam ne kadar ödemesini gerektiğini hesaplayın."

# km_yakıt = input("Aracın kilometrede yaktığı yakıt miktarı:")
# km_yol = input("aracın yaptığı yol:")

# ücret = 40

# print("ödenecek tutar:",ücret * float(km_yakıt)* float(km_yol),sep= "TL")

# # kKullanıcıdan ad,soyad ve numara bilgisini alarak bunları alt alta ekrana yazdırın."

# a = str(input("adınızı girin:"))

# b = str(input("soyadınızı girin:"))

# c = str(input("numaranızı girin:"))

# print("adınız:",a, "soyadınız:",b, "numaranuz:" ,c,sep=" \n ") # sep parametresi ile de yapılabilir.



# # "Kullanıcıdan iki tane sayı isteyin ve bu sayıların değerlerini birbirleriyle değiştirin."

# a = input("birici sayıyı girin:")
# b = input("ikinci sayıyı girin:")   

# a, b = b, a

# print("birinci sayı:", a, "ikinci sayı:", b, sep="\n")



# # "Kullanıcıdan bir dik üçgenin dik olan iki kenarını(a,b) alın ve hipotenüs uzunluğunu bulmaya çalışın.\n"

# uzunk = input("dik üçgenin kısa kenarı:")
# kısak = input("dik üçgenin uzun kenarı:")

# hipo = int(uzunk)**2 + int(kısak)**2

# print("hipo uzunluğu:", hipo ** 0.5, sep="\n")




# adet = 3
# barkod = 567
# fiyat = 49

# siparis = "Ben {} adet {} barkodlu ürünü {:.4f} TL fiyatı ile almak istiyorum."

# print(siparis.format(barkod, barkod, fiyat))

