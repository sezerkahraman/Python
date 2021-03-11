import sqlite3
import time
class Sarki():
    def __init__(self,sarki_ismi,sanatci,album,sirket_ismi,sarki_suresi):
        self.sarki_ismi=sarki_ismi
        self.sanatci=sanatci
        self.album=album
        self.sirket_ismi=sirket_ismi
        self.sarki_suresi=sarki_suresi
    def __str__(self):
        return "sarki={}\nsanatci={}\nalbum={}\nproduksiyon sirketi={}\nsarki suresi={}\n".format(self.sarki_ismi,self.sanatci,self.album,self.sirket_ismi,self.sarki_suresi)
class Sarkilar():
    def __init__(self):
        self.createconnect()


    def createconnect(self):
        self.con=sqlite3.connect("kutuphane1.db")
        self.cursor=self.con.cursor()
        inquiry="Create Table IF NOT EXISTS sarkicilar (sarki_ismi TEXT,sanatci TEXT,album TEXT,sirket_ismi TEXT,sarki_suresi INT)"
        self.cursor.execute(inquiry)
        self.con.commit()

    def disconnect(self):
        self.con.close()


    def showsongs(self):
        inquiry="Select * From sarkicilar"
        self.cursor.execute(inquiry)
        books=self.cursor.fetchall()
        if(len(books)==0):
            print("There are no songs in the library")
        else:
            for i in books:
                song=Sarki(i[0],i[1],i[2],i[3],i[4])
                print(song)


    def inquiry_song(self,name):
        inquiry="Select * From sarkicilar where sarki_ismi= ?"
        self.cursor.execute(inquiry,(name,))
        books=self.cursor.fetchall()
        if(len(books)==0):
            print("There are no songs in the library")
        else:
            song=Sarki([0][1],[0][2],[0][3],[0][4],[0][5])
            print(song)

    def add_song(self,new_song):
        inquiry = "Insert into sarkicilar Values(?,?,?,?,?)"
        self.cursor.execute(inquiry,(new_song.sarki_ismi,new_song.sanatci,new_song.album,new_song.sirket_ismi,new_song.sarki_suresi))
        self.con.commit()



    def delete_song(self,name):
        inquiry = "Delete From sarkicilar where sarki_ismi= ?"
        self.cursor.execute(inquiry,(name,))
        self.con.commit()



    def calculate_song(self):
        inquiry="Select sarki_suresi From sarkicilar"
        self.cursor.execute(inquiry)
        calculate=self.cursor.fetchall()
        total=0
        for i in calculate:
            total=total+i[0]
        print(total)

