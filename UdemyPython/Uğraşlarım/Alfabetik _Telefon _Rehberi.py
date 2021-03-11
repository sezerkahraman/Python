print("""
*****************************
Alfabetik Telefon Rehberi Uygulamama Hoşgeldiniz.
Programdan çıkmak icin q ya basınız
*****************************
Hazırlayan:Sezer Kahraman
""")
while(True):
    kisi = input("Rehberinize eklemek istediğiniz kisileri giriniz=")
    if (kisi == "q"):
        print("Yine bekleriz..")
        print("kaydedilenler",liste)
        break
    else:
        print("Kaydediliyor....")
        liste=[kisi]
        print("Kaydedilen Kisiler=",kisi)

