#Girilen maaş ve zam oranına göre yeni maaş hesaplanır.

maas = float(input("Maaşınızı giriniz:"))
zamOrani = float(input("Zam oranınızı giriniz (%) :"))

zamliMaas = maas + (maas * zamOrani/100)

print ("Güncel Maaşınız:",zamliMaas)
