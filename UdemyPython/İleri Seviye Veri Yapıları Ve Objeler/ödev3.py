# -*- coding: utf-8 -*-
with open("mailler.txt","r",encoding="utf-8") as file:
    for satır in file:
        satır = satır[:-1] ##bunu yapma sebebimiz sondaki \n silmek
        if (satır.endswith(".com") and satır.find("@") != -1):
            print(satır)
