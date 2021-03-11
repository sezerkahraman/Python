def toplama(sezer):
    toplam = 0
    for i in sezer:
        toplam=toplam+i
    return toplam
while True:
    sezer=[]
    sayi=input("Sayi gir")
    sezer.append(sayi)
    if(sayi=="0"):
        break
print("Toplam",toplama(sayi))



