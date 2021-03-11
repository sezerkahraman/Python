class bilgisayar():
    def __init__(self,modeli,markası,işlemcisi,ram,fiyatı,ekran_boyutu):
        self.modeli=modeli
        self.markası=markası
        self.işlemcisi=işlemcisi
        self.ram=ram
        self.fiyatı=fiyatı
        self.ekran_boyutu=ekran_boyutu
    def __str__(self):
        return "Modeli:{}\nMarkası={}\nİşlemcisi={}\nRam={}\nFiyatı={}\nEkran Boyutu={}\n".format(self.modeli,self.markası,self.işlemcisi,self.fiyatı,self.ram,self.ekran_boyutu)
    def __len__(self):
        return len(bilgisayar.fiyatı)
    def indirim(self):
        print("Ürünün eski fiyatı={}".format(self.fiyatı))
        print("İndirim Uygulanıyor.....")
        self.fiyatı=self.fiyatı-(self.fiyatı*10//100)
        print("İndirimli Fiyat={}\n".format(self.fiyatı))
    def indirim_ortaokul(self):
        print("Ürünün eski fiyatı={}".format(self.fiyatı))
        print("İndirim Uygulanıyor.....")
        self.fiyatı = self.fiyatı - (self.fiyatı*20//100)
        print("İndirimli Fiyat={}\n".format(self.fiyatı))
    def indirim_lise(self):
        print("Ürünün eski fiyatı={}".format(self.fiyatı))
        print("İndirim Uygulanıyor.....")
        self.fiyatı = self.fiyatı - (self.fiyatı*35//100)
        print("İndirimli Fiyat={}\n".format(self.fiyatı))
    def indirim_uni(self):
        print("Ürünün eski fiyatı={}".format(self.fiyatı))
        print("İndirim Uygulanıyor.....")
        self.fiyatı = self.fiyatı - (self.fiyatı*50//100)
        print("İndirimli Fiyat={}\n".format(self.fiyatı))
    def kredi(self,tutar):
        pass







pc1=bilgisayar("Dell","i770","i7",8,5000,"17inç")
pc2=bilgisayar("Asus","zenbookpro","i7",16,8000,"16inç")
pc3=bilgisayar("Hp","15da202","i5",4,3000,"16inç")
pc4=bilgisayar("Samsung","S-200","i7",8,4500,"17inç")
print("BÜtçenizi söyleyin sizin için en uygun bilgisayarı bulalım....")
butce=int(input("Lütfen bütçenizi giriniz="))
if(butce>5500):
    print(pc2)
elif(butce>4500):
    print(pc1)
    print(pc2)
elif(butce>4000):
    print(pc1)
    print(pc2)
    print(pc4)
elif(butce>2500):
    print(pc1)
    print(pc2)
    print(pc3)
    print(pc4)
else:
    print("Bütçenize uygun bilgisayar bulunamamıştır\n")
    print("Lütfen indirim kodu almak için gerekli şartları yerine getiriniz....")

    ogrenci_indirimi=int(input("Öğrenciyseniz 1'e değilseniz 0'basınız="))
    if(ogrenci_indirimi==1):
        ne_ogrencisi=int(input("Lütfen eğitim durumunuzu giriniz\n1-İlkokul\n2-Ortaokul\n3-Lise\n4-Üniversite\n"))
        if(ne_ogrencisi==1):
            print("İstediğiniz bilgisayarda kullanacağınız %10 indirim kodunuz 'Banaozel'iyi günlerde kullanınız")
            pc1.indirim()
            pc2.indirim()
            pc3.indirim()
            pc4.indirim()
        if (ne_ogrencisi == 2):
            print("İstediğiniz bilgisayarda kullanacağınız %20 indirim kodunuz 'Banaozel'iyi günlerde kullanınız")
            pc1.indirim_ortaokul()
            pc2.indirim_ortaokul()
            pc3.indirim_ortaokul()
            pc4.indirim_ortaokul()
        if (ne_ogrencisi == 3):
            print("İstediğiniz bilgisayarda kullanacağınız %35 indirim kodunuz 'Banaozel'iyi günlerde kullanınız")
            pc1.indirim_lise()
            pc2.indirim_lise()
            pc3.indirim_lise()
            pc4.indirim_lise()
        if (ne_ogrencisi == 4):
            print("İstediğiniz bilgisayarda kullanacağınız %50 indirim kodunuz 'Banaozel'iyi günlerde kullanınız")
            pc1.indirim_uni()
            pc2.indirim_uni()
            pc3.indirim_uni()
            pc4.indirim_uni()
    else:
        print("Mağazamızda sadece öğrencilere indirim uygulanmaktadır dilerseniz size en uygun bilgisayar kredisine başvuru yapabilirsiniz...\n"
              "Bilgisayar kredisi kullanmak için '1' çıkış yapmak için '0'tuşlayınız ")
        kredi=input("Lütfen tuşlama yapınız=")
        if(kredi=="1"):
            print("*****Mağazımızın kredi departmanına HOŞGELDİNİZ....******\n")
            kredi=int(input("Lütfen ne kadarlık kredi çekmek istediginizi giriniz="))
            if(kredi>=1000 and kredi<=2000):
                print("%20 faizle kredinizi çekebilirsiniz")
                ödeme=kredi+kredi*20//100
                print("Toplam geri ödeyeceğiniz tutar={}".format(ödeme))
            elif (kredi >=2001 and kredi <=3000):
                print("%25 faizle kredinizi çekebilirsiniz")
                ödeme = kredi + kredi * 25 // 100
                print("Toplam geri ödeyeceğiniz tutar={}".format(ödeme))
            elif (kredi >= 3001 and kredi <= 4000):
                print("%30 faizle kredinizi çekebilirsiniz")
                ödeme = kredi + kredi * 30 // 100
                print("Toplam geri ödeyeceğiniz tutar={}".format(ödeme))
            elif (kredi >= 4001 and kredi <= 5000):
                print("%40 faizle kredinizi çekebilirsiniz")
                ödeme = kredi + kredi * 40 // 100
                print("Toplam geri ödeyeceğiniz tutar={}".format(ödeme))











