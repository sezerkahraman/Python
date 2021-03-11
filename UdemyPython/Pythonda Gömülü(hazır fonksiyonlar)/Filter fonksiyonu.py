
##filter() fonksiyonu birinci parametre olarak mutlaka mantıksal değer dönen (True , False)
##bir fonksiyon alır ve liste gibi veritiplerinin her bir elemanına bu fonksiyonunu uygular.
##filter sadece True sonuç çıkaran değerleri alarak bir tane filter objesi döner.
def ciftmi(x):
    if(x%2==0):
        return True
    else:
        return False
sayi1=int(input("Sayiyi giriniz="))
print(ciftmi(sayi1))