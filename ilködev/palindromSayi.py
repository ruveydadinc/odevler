sayi = input("Bir sayı giriniz: ")
palindromSayı = sayi[::-1]
if sayi == palindromSayı :
    print("palindrom bir sayıdır.")
else :
    print("palindrom bir sayı değildir.")