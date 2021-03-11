import os
def masaustu_bulma(isim):
    for klasor_yolu,dosya_adı,dosya_icerigi in os.walk("C:/Users/SEZER/Desktop"):
        for i in dosya_icerigi:
            if(i.endswith(isim)):
                print(i)
isim=input("Lütfen görmek istediginiz dosya uzantılarını giriniz")
masaustu_bulma(isim)

