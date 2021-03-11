"""
Kullanıcıdan iki
tane sayı isteyin ve bu sayıların değerlerini birbirleriyle değiştirin.
"""
a=int(input("Birinci değeri giriniz:"))
b=int(input("ikinci degeri giriniz:"))
print("Degistirilmeden önceki degerler\na={}\nb={}".format(a,b))
a,b=b,a
print("Degistirildikten sonraki degerler\na={}\nb={}".format(a,b))
