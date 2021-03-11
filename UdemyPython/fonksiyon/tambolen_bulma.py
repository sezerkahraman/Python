def tambolen(sayi):
    tambolenler=[]
    for i in range(1,sayi):
        if(sayi%i==0):
            tambolenler.append(i)
    return tambolenler
sayi=input("Sayiyi giriniz=")
sayi=int(sayi)
print(tambolen(sayi))
