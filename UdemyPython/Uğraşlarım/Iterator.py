class Kumanda():
    def __init__(self, kanal_listesi):
        self.kanal_listesi = kanal_listesi  # Kanal Listemiz

    kanallar=kanal_listesi
    def kanallari_goster(self):
        for i in kanallar:
            print(i)
