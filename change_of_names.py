def zmien_nazwy_zdjec(sciezka_katalogu):

    if not os.path.exists(sciezka_katalogu):
        print("Podana ścieżka katalogu nie istnieje.")
        return

    lista_plikow = os.listdir(sciezka_katalogu)

    lista_plikow.sort()


    numeracja = 1

    for stary_nazwa in lista_plikow:

        nowa_nazwa = f"{numeracja}.jpg"


        stara_sciezka = os.path.join(sciezka_katalogu, stary_nazwa)
        nowa_sciezka = os.path.join(sciezka_katalogu, nowa_nazwa)


        os.rename(stara_sciezka, nowa_sciezka)


        numeracja += 1

    print("Zmieniono nazwy plików.")


sciezka_katalogu = "tu wpisać ścieżkę do katalogu"
zmien_nazwy_zdjec(sciezka_katalogu)
