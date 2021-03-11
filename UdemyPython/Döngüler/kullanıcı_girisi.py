print("""
*************
Kullanıcı Giriş Programı
*************
""")
kullanıcı_adı="sezerrkahraman"
parola="Galatasaray"
giris_hakkı=3
while True:
    kullanıcı=input("Kullanıcı adınızı giriniz:")
    parola1=input("Sifrenizi giriniz:")
    if(kullanıcı_adı!=kullanıcı and parola!=parola1):
        print("Hatalı kullanıcı adı veya parola")
        print("Lütfen tekrar deneyiniz.")
        giris_hakkı-=1

    else:
        print("Sisteme başarıyla giriş yaptınız")
        break

    if (giris_hakkı == 0):
        print("Giris hakkınız bitti")
        break