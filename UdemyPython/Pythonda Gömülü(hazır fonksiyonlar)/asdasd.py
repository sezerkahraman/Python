isim = ["Kerim","Tarik","Ezgi","Kemal","Ilkay","S�kran","Merve"]

soyisim = ["Y�lmaz","�zt�rk","Da�deviren","Atat�rk","Dikmen","Kaya","Polat"]

liste = list(zip(isim,soyisim))

liste.sort()

for i,j in liste:
    print(i,j)