birler=["","Bir","İki","Uc","Dort","Bes","Altı","Yedi","Sekiz","Dokuz"]
onlar=["","On","Yirmi","Otuz","Kırk","Elli","Atmış","Yetmiş","Seksen","Doksan"]
def sayi_okuma(sayi):
    birinci=sayi%10
    ikinci=sayi//10
    return onlar[ikinci]+" "+birler[birinci]
sayi=int(input("okunmasini istediginiz sayiyi giriniz="))
print(sayi_okuma(sayi))
