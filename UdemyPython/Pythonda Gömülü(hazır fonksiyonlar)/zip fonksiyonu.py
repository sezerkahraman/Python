#liste1 = [1,2,3,4,5]
#liste2 = [6, 7, 8, 9, 10, 11]


# sonucu [(1,6),(2,7),(3,8),(4,9),(5,10)] yapmaya çalışalım.

i = 0
sonuç = list()
#while (i < len(liste1) and i < len(liste2)):
 #   sonuç.append((liste1[i], liste2[i]))

  #  i += 1
#print(sonuç)

##Peki böyle uzun bir işlemi zip fonksiyonuyla nasıl yaparız ?
# İsterseniz zip fonksiyonunun kullanımını direk örnek üzerinden görelim.
#print(list(zip(liste1,liste2)))
liste1=["sezer","Latif","Zeynep"]
liste2=[24,51,16]
for i,j in zip(liste1,liste2):
    print(i,j)