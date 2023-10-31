sayi1 = float(input("Birinci Sayıyı Giriniz: "))
sayi2 = float(input("İkinci Sayıyı Giriniz: "))
sayi3 = float(input("Üçüncü Sayıyı Giriniz: "))


if sayi1 >= sayi2 and sayi1 >= sayi3:
    enBuyukSayi = sayi1
elif sayi2 >= sayi3 and sayi2 >= sayi1:
    enBuyukSayi = sayi2
else:
    enBuyukSayi = sayi3

    print("En Büyük Sayı: ", enBuyukSayi)