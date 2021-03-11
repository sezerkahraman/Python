def asal_sayi(sayi):
   if(sayi==1):
       return False
   elif(sayi==2):
       return True
   else:
       for i in range(2,sayi):
            if(sayi%i==0):
                return False

       return True

while True:
    sayi=input("Bir sayi giriniz=")
    if(sayi=="q"):
        print("Programdan çıktınız")
        break
    else:
        sayi=int(sayi)
        if(asal_sayi(sayi)):
            print("Asal sayi girdiniz")
        else:
            print("Asal sayi degildir")

