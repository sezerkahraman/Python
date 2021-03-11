print("""
****************
Faktöriyel bulma programımıza hoşgeldiniz..
Çıkmak için q basınız
Hazırlayan:Sezer Kahraman
****************
""")
faktoriyel=1
while True:
    sayı=input("Sayı:")
    if(sayı=="q"):
        print("Program sonlandırılıyor")
        break
    else:
        sayı=int(sayı)
        for i in range(1,sayı+1):
            faktoriyel=faktoriyel*i
        print("Hesaplamak istediginiz faktöriyel degeri {}'dir".format(faktoriyel))
