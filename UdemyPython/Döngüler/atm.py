print("""
***************
Sezerbank'a hoşgeldiniz...
    1-Bakiye sorgulama
    2-Para Çekme
    3-Para Yatırma
Çıkmak için lütfen q tuşuna basınız..
****************
""")
bakiye=2000
while True:
    secim=input("İşlemi seciniz:")
    if(secim=="q"):
        print("Yine bekleriz")
        break
    elif(secim=="1"):
        print("Mevcut bakiyeniz {}'tldir".format(bakiye))

    elif(secim=="2"):
        tutar=int(input("Lütfen cekmek istediginiz tutarı giriniz:"))

        if(bakiye-tutar<0):
            print("Yetersiz bakiye")
            continue
        bakiye =bakiye-tutar
    elif(secim=="3"):
        yatırılacak=int(input("Lütfen yatırmak istediğiniz tutarı giriniz:"))
        bakiye=bakiye+yatırılacak

    else:
        print("Hatalı tuşlama yaptınız lütfen tekrar deneyiniz")
        continue


