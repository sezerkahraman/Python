def karekter(str):
    for i in str:
        if(i=="ğ"):
            return True
            break
metin=input("Sezer: ")
if(karekter(metin)==1):
    print("ğ harfi vardır")
else:
    print("ğ harfi yoktur")