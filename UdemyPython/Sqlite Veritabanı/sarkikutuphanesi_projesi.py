from sarki import *
print("""
*****************************
Welcome to Songs-Library

*****************************
Operations
1-Show Songs
2-Inquiry Song
3-Add Songs
4-Delete Songs
5-Calculate Total Song Times
exit for 'q' enter
""")
sarkilar=Sarkilar()
while True:
    selection=input("Select Operation=")

    if(selection=="q"):
        print("Program exits")
        break

    if(selection=="1"):
        sarkilar.showsongs()

    if(selection=="2"):
        name=input("the song you want to question?")
        sarkilar.inquiry_song(name)

    if(selection=="3"):
        sarki_ismi=input("the song you want to add=")
        sanatci=input("Singer's name=")
        album=input("Song album=")
        sirket_ismi=input("Company name=")
        sarki_suresi=int(input("Song time"))

        new_song=Sarki(sarki_ismi,sanatci,album,sirket_ismi,sarki_suresi)
        print("Song is inserting....")
        time.sleep(3)
        sarkilar.add_song(new_song)
        print("Song was inserted.")

    if(selection=="4"):
        name=input("The song you want to delete=")
        sarkilar.delete_song(name)

    if(selection=="5"):
        sarkilar.calculate_song()


