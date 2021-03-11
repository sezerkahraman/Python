def tek_cift(a):
    if(a%2==0):
        return ("{} sayısı çift sayidir".format(a))
    else:
        raise ValueError
sayi=int(input("Bir sayi giriniz="))
print(tek_cift(sayi))

