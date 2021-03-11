print("""
**************
Harf Notu Hesaplama Programı
**************
""")
vize1=int(input("1.vize notunuzu giriniz:"))
vize2=int(input("2.vize notunuzu giriniz:"))
final=int(input("Final notunuzu:"))

toplam_not=(vize1*0.3)+(vize2*0.3)+(final*0.4)

if(toplam_not>=90):
    print("AA")
elif(toplam_not>=85):
    print("BA")
elif(toplam_not>=80):
    print("BB")
elif(toplam_not>=75):
    print("CB")
elif(toplam_not>=70):
    print("CC")
elif(toplam_not>=65):
    print("DC")
elif(toplam_not>=60):
    print("DD")
elif(toplam_not>=55):
    print("FD")
elif(toplam_not<=55):
    print("FF")