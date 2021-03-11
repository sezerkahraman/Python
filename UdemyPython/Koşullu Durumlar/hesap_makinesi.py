print("""***********
Hesap makinası Programı
İşlemler:
1-Toplama İşlemi

2-Çıkarma İşlemi

3-Çarpma İşlemi

4-Bölme işlemi
*************
""")
a=int(input("Birinci sayiyi giriniz:"))
b=int(input("İkinci sayiyi giriniz:"))
islem=input("İslemi giriniz:")

if(islem=="1"):
    print("{} ile {}'in toplamı {}".format(a,b,a+b))
elif(islem=="2"):
    print("{} ile {}'in farkı {}".format(a,b,a-b))
elif(islem=="3"):
    print("{} ile {}'in çarpımı {}".format(a,b,a*b))
elif(islem=="4"):
    print("{} ile {}'in bölümü {}".format(a,b,a/b))
else:
    print("Hatalı işlem girdiniz")