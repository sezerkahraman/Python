toplam=0
while True:
    sayi=input("Bir sayi giriniz")
    if(sayi=="q"):
        break
    sayi=int(sayi)
    toplam+=sayi
print(toplam)