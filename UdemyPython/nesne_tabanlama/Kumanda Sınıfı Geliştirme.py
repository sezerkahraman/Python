class Kumanda():
    def __init__(self,tv_durumu="Kapalı",ses_durumu=0,kanal_listesi=["Trt"]):
        self.tv_durumu=tv_durumu
        self.ses_durumu=ses_durumu
        self.kanal_listesi=kanal_listesi
    def tv_kapat(self):
        print("Tv kapatalıyor")
        self.tv_durumu="Kapalı"
    def tv_ac(self):
        print("Tv açılıyor....")
        self.tv_durumu="Açık"

    def ses_ayarı(self):
        while True:
            karakter = input("Sesi yükseltmek için '<',sesi düşürmek için '>' basınız=")
            if (karakter ==">"):
                if (self.ses_durumu != 0):
                    self.ses_durumu -= 1
                    print("Ses:", self.ses_durumu)
            elif (karakter =="<"):
                if (self.ses_durumu != 32):
                    self.ses_durumu += 1
                    print("Ses:", self.ses_durumu)
            else:
                print("Ses güncellendi=", self.ses_durumu)
                break
    def kanal_ekle(self,yeni_kanal):
        print("Kanal ekleniyor...")
        self.kanal_listesi.append(yeni_kanal)
        print("Kanal eklendi...")
    def __str__(self):
        return "Tv durumu={}\nSes Durumu={}\nKanallar={}".format(self.tv_durumu,self.ses_durumu,self.kanal_listesi)
    def __len__(self):
        return len(self.kanal_listesi)
    def kanaldegis(self,i):
        print("Geçtiginiz kanal=",self.kanal_listesi[i-1])






kumanda=Kumanda()
print("""
Televizyon Uygulaması
İşlemler
1-Tv açma
2-Tv kapatma
3-Sesİ Azaltma veya arttırma
4-Kanal ekleme
5-Kanal sayısını öğrenme
6-Televizyon bilgileri
7-Kanal degistirme
Programdan çıkmak için q'ya basınız.......
""")
while True:
    işlem=input("İşlemi seçiniz=")
    if(işlem=="q"):
        print("Programdan çıkılıyor...")
        break
    if(işlem=="1"):
        kumanda.tv_ac()
    elif(işlem=="2"):
        kumanda.tv_kapat()
    elif(işlem=="3"):
        kumanda.ses_ayarı()
    elif(işlem=="4"):
        x=1
        kanallar=input("Eklenecek kanalları araya ','işareti koyarak ekleyiniz = ")
        eklenecekler=kanallar.split(",")

        for i in eklenecekler:
            kumanda.kanal_ekle(i)
    elif(işlem=="5"):
        print(len(kumanda))
    elif(işlem=="6"):
        print(kumanda)
    elif(işlem=="7"):
        print(kumanda.kanal_listesi)
        hangikanal=int(input("Geçmek istediğiniz kanalın  numarasını tuşlayınız..="))
        kumanda.kanaldegis(hangikanal)


    else:
        print("Hatalı işlem girdiniz....")






