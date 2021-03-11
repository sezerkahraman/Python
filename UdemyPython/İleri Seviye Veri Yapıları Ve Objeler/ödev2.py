bas_harfler=""
with open("siir.txt","r",encoding="utf-8")as file:
        for i in file:
            bas_harfler=bas_harfler+i[0]
print(bas_harfler)
