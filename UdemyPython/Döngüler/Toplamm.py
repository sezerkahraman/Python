print("""
********************
Programa Hoşgeldiniz
Hazırlayan:Sezer Kahraman
********************
""")
toplam=0
while(True):
    sayı=input("Toplamak istediğiniz sayıyı giriniz:")
    if (sayı == "q"):
        print("Programdan çıkış yapılıyor")
        break
    sayı=int(sayı)
    toplam+=sayı
print("Girdiginiz sayıların toplamı:",toplam)
