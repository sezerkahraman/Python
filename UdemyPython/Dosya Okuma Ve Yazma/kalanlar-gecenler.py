qalanlar = list()
keceneler = list()


def not_hesabla(satir):
    satir = satir[:-1]
    liste = satir.split(",")
    ad = liste[0]
    not1 = int(liste[1])
    not2 = int(liste[2])
    not3 = int(liste[3])
    son_not = not1 * 0.3 + not2 * 0.3 + not3 * 0.4

    if son_not >= 90:
        harf = "AA"
    elif son_not >= 85:
        harf = "BA"
    elif son_not >= 80:
        harf = "BB"
    elif son_not >= 75:
        harf = "CB"
    elif son_not >= 70:
        harf = "CC"
    elif son_not >= 65:
        harf = "DC"
    elif son_not >= 60:
        harf = "DD"
    elif son_not >= 55:
        harf = "FD"
    else:
        harf = "FF"

    if son_not >= 55:
        keceneler.append(ad + "----------------->" + harf + "\n")
    else:
        qalanlar.append(ad + "----------------->" + harf + "\n")


with open("dosya.txt", "r", encoding="utf-8") as file:
    eklenecekler = []
    for i in file:
        eklenecekler.append(not_hesabla(i))
    with open("qalanlar", "w", encoding="utf-8") as file2:
        for i in qalanlar:
            file2.write(i)
    with open("kecenler", "w", encoding="utf-8") as file3:
        for i in keceneler:
            file3.write(i)