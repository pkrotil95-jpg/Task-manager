ukoly: list[dict] = []


def pridat_ukol(ukoly: list[dict]) -> list[dict]:
    """Přidá nový úkol do seznamu úkolů. Obě pole jsou povinná."""
    while True:
        nazev = input("Zadejte název nového úkolu: ").strip()
        if not nazev:
            print("Chyba: Název ani popis nesmí být prázdné. Zkuste to znovu.")
            continue

        popis = input("Zadejte popis úkolu: ").strip()
        if not popis:
            print("Chyba: Název ani popis nesmí být prázdné. Zkuste to znovu.")
            continue

        ukoly.append({"nazev": nazev, "popis": popis})
        print(f"Úkol '{nazev}' byl úspěšně přidán.")
        break

    return ukoly


def zobrazit_ukoly(ukoly: list[dict]) -> None:
    """Zobrazí všechny úkoly v seznamu."""
    if not ukoly:
        print("Seznam úkolů je prázdný.")
    else:
        print("\nSeznam úkolů:")
        for i, ukol in enumerate(ukoly, start=1):
            print(f"  {i}. {ukol['nazev']} - {ukol['popis']}")


def odstranit_ukol(ukoly: list[dict]) -> list[dict]:
    """Odstraní úkol ze seznamu podle jeho čísla."""
    zobrazit_ukoly(ukoly)
    if not ukoly:
        return ukoly

    while True:
        try:
            cislo = int(input("Zadejte číslo úkolu, který chcete odstranit: "))
            if 1 <= cislo <= len(ukoly):
                odstranen = ukoly.pop(cislo - 1)
                print(f"Úkol '{odstranen['nazev']}' byl úspěšně odstraněn.")
                break
            else:
                print(f"Neplatné číslo úkolu. Zadejte číslo od 1 do {len(ukoly)}.")
        except ValueError:
            print("Zadejte prosím platné číslo.")

    return ukoly


def hlavni_menu() -> None:
    """Hlavní menu správce úkolů."""
    seznam = ukoly

    while True:
        print("\nSprávce úkolů - Hlavní menu")
        print("1. Přidat nový úkol")
        print("2. Zobrazit všechny úkoly")
        print("3. Odstranit úkol")
        print("4. Konec programu")
        volba = input("Vyberte možnost (1-4): ").strip()

        if volba == "1":
            seznam = pridat_ukol(seznam)
        elif volba == "2":
            zobrazit_ukoly(seznam)
        elif volba == "3":
            seznam = odstranit_ukol(seznam)
        elif volba == "4":
            print("Program byl ukončen. Na shledanou!")
            break
        else:
            print("Neplatná volba. Zadejte prosím číslo mezi 1 a 4.")


if __name__ == "__main__":
    hlavni_menu()
