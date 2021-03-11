##map() fonksiyonu ilk parametre olarak bir tane fonksiyon objesi alır.
# (Fonksiyonlar da birer obje olduğu için başka bir fonksiyona gönderilebilir.)
# 2. parametre olarak da bir tane iterasyon yapılacak veritipi alarak ,
# gönderilen fonksiyonu her bir eleman üzerinde uygulayarak sonuçları bir map objesi olarak döner.
#Örneklerimize geçersek bu fonksiyonun işlevini daha iyi anlayacağız.
def ikiylecarp(x):
    x=int(x)
    return x*2
sayi1=input("SAYİ=")
print(list(map(ikiylecarp,sayi1)))
