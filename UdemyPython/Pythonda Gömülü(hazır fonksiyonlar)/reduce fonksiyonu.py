##uce() fonksiyonu değer olarak aldığı fonksiyonu soldan başlayarak listenin
# ilk 2 elemanına uygular ve daha sonra çıkan sonucu listenin 3. elemanına uygular
# ve bu şekilde devam ederek liste bitince bir tane değer döner.
# Anlamak için örneğimize ve görselimize bakalım.
from functools import reduce
##def topla(x,y):
  ##  return x+y
##print(reduce(topla,[1,5,8,10]))

def maksimumbul(x,y):
    if(x>y):
        return x
    else:
        return y
eklenecekler=[]
sayi1=input("Listeye eklenek sayıyı giriniz=")
eklenecekler.append(sayi1)
sayi2=input("Listeye eklenek sayıyı giriniz=")
eklenecekler.append(sayi2)
sayi3=input("Listeye eklenek sayıyı giriniz=")
eklenecekler.append(sayi3)
sayi4=input("Listeye eklenek sayıyı giriniz=")
eklenecekler.append(sayi4)
print(reduce(maksimumbul,eklenecekler))