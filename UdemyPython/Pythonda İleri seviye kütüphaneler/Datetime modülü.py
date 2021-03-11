from _datetime import datetime
import locale ##gunu ve ayi turkce gormek icin bu kutuphaneyi ekledik

locale.setlocale(locale.LC_ALL,"") ##ve bu modulu kullandık
#print(datetime.now()) ##bize suanki zamani ve tarihi verir
suan=datetime.now()
print(suan.year) #sadece yili verir
print(suan.month) #sadece ayi verir
print(suan.day)  #sadece gunu verir
print(datetime.ctime(suan)) ##boyle yaparsak  daha guzel bir cikti verir
print(datetime.strftime(suan,"%Y")) ##sadece yil bilgisini verir
print(datetime.strftime(suan,"%B")) ##sadece ay bilgisini verir
print(datetime.strftime(suan,"%A")) ##gun ismini verir
print(datetime.strftime(suan,"%X")) ##saat bilgisini verir
print(datetime.strftime(suan,"%D")) ##suanin tarihini verir

tarih=datetime(1998,10,11)
tarih2=datetime(1998,7,31)
print(tarih2-tarih) ##tarihler arasindaki farki bulduk