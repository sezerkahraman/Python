toplam=[]
def toplama():
    sonuc=0
    for i in toplam:
        sonuc=sonuc+i
    return sonuc
while True:
    sayi=int(input("Toplanacak sayilari giriniz"))
    toplam.append(sayi)
    print("Çıkmak için 0'a basınız")
    if(sayi==0):
        break
print("Toplam sonucu= ",toplama())