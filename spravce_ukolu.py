ukoly = []


def pridat_ukol():
    """Přidá nový úkol do seznamu úkolů. Obě pole jsou povinná."""
    while True:
        nazev = input("Zadejte název nového úkolu: ").strip()
        popis = input("Zadejte popis úkolu: ").strip()

        if not nazev or not popis:
            print("Zadání prázdného pole")
        else:
            ukoly.append({"název": nazev, "popis": popis})
            print(f"Úkol '{nazev}' byl úspěšně přidán.")
            break


def zobrazit_ukoly():
    """Zobrazí všechny úkoly v seznamu."""
    if not ukoly:
        print("Seznam úkolů je prázdný.")
    else:
        print("\nSeznam úkolů:")
        for i, ukol in enumerate(ukoly, start=1):
            print(f"  {i}. {ukol['název']} - {ukol['popis']}")


def odstranit_ukol():
    """Odstraní úkol ze seznamu podle jeho čísla."""
    zobrazit_ukoly()
    if not ukoly:
        return
    try:
        cislo = int(input("Zadejte číslo úkolu, který chcete odstranit: "))
        if 1 <= cislo <= len(ukoly):
            odstranen = ukoly.pop(cislo - 1)
            print(f"Úkol '{odstranen['název']}' byl úspěšně odstraněn.")
        else:
            print("Neplatné číslo úkolu.")
    except ValueError:
        print("Zadejte prosím platné číslo.")


def hlavni_menu():
    """Hlavní menu správce úkolů."""
    while True:
        print("\nSprávce úkolů - Hlavní menu")
        print("1. Přidat nový úkol")
        print("2. Zobrazit všechny úkoly")
        print("3. Odstranit úkol")
        print("4. Konec programu")
        volba = input("Vyberte možnost (1-4): ").strip()

        if volba == "1":
            pridat_ukol()
        elif volba == "2":
            zobrazit_ukoly()
        elif volba == "3":
            odstranit_ukol()
        elif volba == "4":
            print("Program byl ukončen. Na shledanou!")
            break
        else:
            print("Neplatná volba. Zadejte prosím číslo mezi 1 a 4.")


if __name__ == "__main__":
    hlavni_menu()
