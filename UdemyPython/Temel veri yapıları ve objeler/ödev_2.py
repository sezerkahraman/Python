"""
Kullanıcıdan aldığınız boy ve kilo değerlerine göre kullanıcının beden kitle indeksini bulun.
Beden Kitle İndeksi : Kilo / Boy(m) Boy(m)

a=int(input("Kilonuzu giriniz:"))
b=int(input("boyunuzu giriniz"))
endeks=a/b*b
print("Beden kitle endeksiniz = {}".format(endeks))

boy = float(input("Boy:"))
kilo = int(input("Kilo:"))

print("Beden Kitle İndeksi:",kilo / (boy ** 2))
"""
a=int(input("Kilonuzu giriniz:"))
b=float(input("boyunuzu giriniz:"))
endeks=a/(b*b)
print("Beden kitle endeksiniz = {}".format(endeks))