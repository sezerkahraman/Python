def mukemmel_sayi(sayi):
    toplam = 0
    for i in range(1,sayi):
        if(sayi%i==0):
            toplam=toplam+i
    return toplam==sayi

for i in range(1,1001):
    if(mukemmel_sayi(i)):
        print("Mükemmel sayi",i)
