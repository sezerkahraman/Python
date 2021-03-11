class hayvan():
    def __init__(self,tür,ayak_sayisi,renk):
        self.tür=tür
        self.ayak_sayisi=ayak_sayisi
        self.renk=renk
    def bilgilerigoster(self):
        print("Türü={}\nAyak Sayısı={}\nRenk={}".format(self.tür,self.ayak_sayisi,self.renk))
class köpek(hayvan):
    def __init__(self,tür,ayak_sayisi,renk,omurgalı):
        super().__init__(tür,ayak_sayisi,renk)
        self.omurgalı=omurgalı
    def bilgilerigoster(self):
        print("Türü={}\nAyak Sayısı={}\nRenk={}\nOmurgalı={}\n".format(self.tür,self.ayak_sayisi,self.renk,self.omurgalı))
hayvan_tanı=köpek("Pitbull","4","Siyah","Omurgalı",)
hayvan_tanı.bilgilerigoster()
class kus(hayvan):
    def __init__(self,tür,ayak_sayısı,renk,kanat):
        super().__init__(tür,ayak_sayısı,renk)
        self.kanat=kanat
    def bilgilerigoster(self):
        print("Türü={}\nAyak Sayısı={}\nRenk={}\nKanat={}\n".format(self.tür,self.ayak_sayisi,self.renk,self.kanat))
kuş=kus("Papağan","2","Beyaz","Kanatlı")
kuş.bilgilerigoster()
class at(hayvan):
    def __init__(self,türü,ayak_sayisi,renk,memeli):
        super().__init__(türü,ayak_sayisi,renk)
        self.memeli=memeli
    def bilgilerigoster(self):
        print("Türü={}\nAyak sayısı={}\nRenk={}\nMemeli={}".format(self.tür,self.ayak_sayisi,self.renk,self.memeli))
at=at("At","4","Beyaz","Evet")
at.bilgilerigoster()

