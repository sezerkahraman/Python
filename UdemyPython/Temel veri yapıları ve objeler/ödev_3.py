"""
Bir aracın kilometrede ne kadar yaktığı ve kaç kilometre yol yaptığı
bilgilerini alın ve sürücünü toplam ne kadar ödemesini gerektiğini hesaplayın.
"""
yakdıgı=float(input("Kilometrede ne kadar yakıyor:"))
kilometre=float(input("Kaç kilometre yol yapıyor:"))
ödenmesi_gereken=yakdıgı*kilometre
print("Sürücünün ödemesi gereken miktar ={}tl".format(ödenmesi_gereken))