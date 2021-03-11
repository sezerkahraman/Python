sözlük={"Sezer":"05059156880"
        ,"Aysegül":"05069926382",
        "Latif":"05327056537"}
kisi=input("Lütfen telefon numarasını öğrenmek için bir kişi adını giriniz:")
if(kisi=="Sezer"):
    print("{}: {}".format(kisi,sözlük[kisi]))
elif(kisi=="Aysegul"):
    print("{}: {}".format(kisi,sözlük[kisi]))
elif(kisi=="Latif"):
    print("{}: {}".format(kisi, sözlük[kisi]))
else:
    print("Aradıgınız kisi rehberde mevcut değil.")

