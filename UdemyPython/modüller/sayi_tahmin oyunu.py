import random
import time
print("Sayi tahimini oyununa hoşgeldiniz")

rastgele_sayi=random.randint(1,40)
tahmin_hakkı=7
while True:
    tahmin=int(input("Tahmininizi giriniz:"))
    if(tahmin<rastgele_sayi):
        print("Bilgileriniz kontrol ediliyor")
        time.sleep(1)
        print("Daha yüksek bir sayi giriniz.....")
        tahmin_hakkı-=1
    elif(tahmin>rastgele_sayi):
        print("Bilgileriniz kontrol ediliyor")
        time.sleep(1)
        print("Daha düsük bir sayi giriniz.....")
        tahmin_hakkı -= 1
    else:
        print("Bilgileriniz sorgulanıyor...")
        time.sleep(1)
        print("Tebrikler Sayımız",rastgele_sayi)
        break
    if(tahmin_hakkı==0):
        print("Tahmin hakkınız bitmiştir")
        break