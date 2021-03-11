print("""
**************
Kullanıcı Girişi
**************
""")
sys_kullanıcıadı="sezerrkahraman"
sys_parola="galatasaray"
kullanıcı_adı=input("Kullanıcı adınızı giriniz:")
parola=input("Parolanızı giriniz:")
if(sys_kullanıcıadı==kullanıcı_adı and sys_parola==parola):
    print("Hoşgeldiniz")
else:
    print("Hatalı kullanıcı adı veya parola")