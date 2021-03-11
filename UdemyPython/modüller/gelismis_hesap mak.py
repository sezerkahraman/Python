import math

print("**********Gelişmiş Hesap Makinama Hoşgeldiniz**********")
print("Hazırlayan:Sezer Kahraman")
while True:
    print("Lütfen yapmak istediginiz işlemi seçiniz...\n1-Toplama\n2-Çıkarma\n3-çarpma\n4-Bölme\n5-Faktoriyel Hesaplama\n6-Üs alma\n7-Dereceden radyana dönüştürme\n8-Radyandan Dereceye dönüştürme\n9-Sin\n10-Cos\n11-Tan\n12-Pi sayısı\n13-Karekök bulma")
    secim=int(input("Secim="))
    sayi=[]
    while(secim<2):
        toplam = 0
        sayilar=int(input("Toplamak istediginiz sayiları giriniz:      Çıkmak için 0 tusuna basınız"))
        sayi.append(sayilar)
        for i in sayi:
            toplam=toplam+i

        if(sayilar==0):
            print("Cıkıs yaptınız.........")
            print("Girdiginiz sayilarin toplamı=",toplam)
    while(secim>1 and secim<3):
        sayı1=int(input("Sayiyi giriniz="))
        sayı2=int(input("Sayiyi giriniz="))
        print("Çıkartma işleminin sonucu= ",sayı1-sayı2)
        break
    while(secim>2 and secim<4):
        sayı1 = int(input("Sayiyi giriniz="))
        sayı2 = int(input("Sayiyi giriniz="))
        print("Çarpma işleminin sonucu= ", sayı1*sayı2)
        break
    while(secim>3 and secim<5):
        sayı1 = int(input("Sayiyi giriniz="))
        sayı2 = int(input("Sayiyi giriniz="))
        print("Bolme işleminin sonucu= ", sayı1 / sayı2)
        break
    while(secim>4 and secim<6):
        faktoriyel=int(input("Faktoriyelinin hesaplanmasını istediginiz sayiyi giriniz="))
        print("Faktoriyel sonucu=",math.factorial(faktoriyel))
        break
    while(secim>5 and secim<7):
        üstalma=int(input("Tabanı giriniz="))
        üstalma1=int(input("Üstü giriniz="))
        print("İşlemin sonucu= ",pow(üstalma,üstalma1))
        break
    while(secim>6 and secim<8):
        derece=int(input("Radyana dönüştürmek istediğiniz derececeyi giriniz="))
        print("Radyanı= ",math.radians(derece))
        break
    while(secim>7 and secim<9):
        radyan = int(input("Dereceye dönüştürmek istediğiniz radyanı giriniz="))
        print("Radyanı= ", math.degrees(radyan))
        break
    while(secim>8 and secim<10):
        derece=int(input("Derece="))
        print("sin {} =".format(derece),math.sin(derece))
        break
    while(secim>9 and secim<11):
        derece = int(input("Derece="))
        print("cos {} =".format(derece), math.cos(derece))
        break
    while(secim>10 and secim<12):
        derece = int(input("Derece="))
        print("tan {} =".format(derece), math.tan(derece))
        break
    while(secim>11 and secim<13):
        print("Pi sayısı =",math.pi)
        break
    while(secim>12 and secim<14):
        sayi=int(input("Karekökünü almak istediğiniz sayiyi giriniz"))
        print("Sayinin karekökü = ",math.sqrt(sayi))
        break









