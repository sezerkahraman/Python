print("""
****************
Beden kitle hesaplama programına hoşgeldiniz
****************
""")
a=float(input("Kilonuzu giriniz:"))
b=float(input("Boyunuzu giriniz:"))
endeks=a/(b*b)
if(endeks>30):
    print("Obez")
elif(endeks>25):
    print("Fazla kilolu")
elif(endeks>18.5):
    print("Normal")
elif(endeks<18.5):
    print("Zayıf")

