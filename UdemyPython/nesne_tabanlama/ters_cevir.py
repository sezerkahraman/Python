def terscevir(s):
    if(type(s)!=str):
        raise ValueError("Lütfen string bir ifade giriniz")
    else:
            return s[::-1]
kelime=input("Lütfen ters çevrilecek kelimeyi giriniz")
kelime=type(str)
print(terscevir(kelime))