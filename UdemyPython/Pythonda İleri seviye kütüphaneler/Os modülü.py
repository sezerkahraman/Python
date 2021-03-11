import os
from datetime import datetime
## print(os.getcwd()) ##bulundugumuz dizinin adresini verir
# os.mkdir("deneme1") ##bulundugumuz dizinde bir dosya oluşturur
# os.makedirs("deneme2/deneme3") ##burdada önce deneme2 klasorunu olusturur ardından icine deneme3'u olştr.
# os.rmdir("deneme1") yaparsak deneme1 klasoru silinir
# os.removedirs("deneme2/deneme3") hem deneme2 yi siler hemde içindeki klasoru
## os.rename("test.txt","test2.txt") ## test.txt olan dosyanın adını test2.txt yaptı
## print(os.stat("test2.txt").st_mtime) ##boyle yaparak dosyanın degistirilme zamanını saniye cinsinden goruyoruz
## print((datetime.fromtimestamp(os.stat("test2.txt").st_mtime))) ##dosyanın degistirilme zamanını saat cinsinden elde ettik
## print(os.walk("C:/Users/user/Desktop"))
for klasor_yolu,klasor_ismi,dosya_isimler in os.walk("C:/Users/SEZER/Desktop"):
   # print("Klasor yolu",klasor_yolu)
   # print("Klasor ismi",klasor_ismi)
   #print("dosya işlemleri",dosya_isimler)
   #print("*****************")
   for i in dosya_isimler: ##sadece dosya isimlerini görmek için
       print(i)
        #if(i.endswith(".txt")): ##eger sadece txt i ile biten dosyaları görmek için
            #print(i)