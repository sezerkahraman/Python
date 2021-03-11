print("""
***************
En büyük sayıyı ekrana yazdıran program
***************
""")
a=int(input("Birinci sayıyı giriniz:"))
b=int(input("İkinci sayiyi giriniz:"))
c=int(input("Ucuncu sayiyi giriniz:"))
if(a>b and a>c):
    print("En büyük sayı {}'dır".format(a))
elif(b>a and b>c):
    print("En büyük sayi {}'dir".format(b))
elif(c>a and c>b):
    print("En büyük sayi {}'dir".format(c))