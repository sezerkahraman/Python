def dikdörtgen_alani(uzunkenar,kisakenar):
    alan=uzunkenar*kisakenar
    return alan

uzunkenar=int(input("Uzun kenarini giriniz:"))
kisakenar=int(input("Kisa kenarini giriniz:"))
print("Dikdörtgen alani=",dikdörtgen_alani(uzunkenar,kisakenar))