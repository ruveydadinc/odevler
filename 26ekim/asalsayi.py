# Asal sayı sadece 1'e ve kendisine bölünebilir, her zaman 1'den büyüktür.

sayi= int(input("Sayı giriniz: "))
if sayi > 1:
    for i in range(2,sayi):
        if (sayi % i ) == 0 :
            print(sayi, "Asal değildir.")
            break
    else:
        print(sayi,"Asaldır.")
else: 
    print(sayi,"Asal değildir.")

 