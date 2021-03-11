print("**********Hazırlayan=Sezer Kahraman")
sayi=int(input("Bir sayi giriniz:"))
i=1
toplam=0
while(i < sayi):
    if(sayi%i==0):
        toplam=toplam+i
    i=i+1
if(toplam==sayi):
    print(sayi," mukemmel sayıdır")
else:
    print(sayi,"mukemmel sayı degildir")