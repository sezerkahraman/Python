tektoplam = 0
cifttoplam = 0
ciftsayac = 0
teksayac = 0
ciftortalama = 0
tekortalama = 0
while True:
    tercih=input("Çıkmak için y ye basınız")
    if(tercih=="y"):
        break
    else:
        sayi = input("Bir sayi giriniz")
        ara = int(sayi)
        if (ara % 2 == 0):
            cifttoplam = cifttoplam + ara
            ciftsayac = ciftsayac + 1
            ciftortalama = cifttoplam / ciftsayac

        else:
            tektoplam = tektoplam + ara
            teksayac = teksayac + 1
            tekortalama = tektoplam / teksayac


print(ciftortalama)
print(tekortalama)

