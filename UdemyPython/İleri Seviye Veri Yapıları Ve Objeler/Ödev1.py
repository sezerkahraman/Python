#s="ProgramlamaÖdeviİleriSeviyeVeriYapılarıveObjeleripynb"
#yeni_kelime=s.strip("")
#küme=set()
#kac_defa=dict()
#for i in yeni_kelime:
 #   küme.add(i)
#for i in küme:
 #   if(i in kac_defa):
  #      kac_defa[i]+=1
   #   else:
    #    kac_defa[i]=1
#for kelime,sayı in kac_defa.items():
 #   print("{} kelimesi {} defa geçiyor".format(kelime,sayı))
s = "ProgramlamaÖdeviİleriSeviyeVeriYapılarıveObjeleripynb"
frekans = dict()

for karakter in s:
    if (karakter in frekans):
        frekans[karakter] += 1
    else:
        frekans[karakter] = 1
for i, j in frekans.items():
    print(i, ":", j)