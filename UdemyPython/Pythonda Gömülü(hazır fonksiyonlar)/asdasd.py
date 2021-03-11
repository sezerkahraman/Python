isim = ["Kerim","Tarik","Ezgi","Kemal","Ilkay","Sükran","Merve"]

soyisim = ["Yýlmaz","Öztürk","Daðdeviren","Atatürk","Dikmen","Kaya","Polat"]

liste = list(zip(isim,soyisim))

liste.sort()

for i,j in liste:
    print(i,j)