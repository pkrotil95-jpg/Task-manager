# Task Manager

Jednoduchý správce úkolů pro příkazový řádek napsaný v Pythonu. Program umožňuje přidávat, zobrazovat a odstraňovat úkoly přímo v terminálu.

---

## Co program dělá

Program nabízí interaktivní textové menu se čtyřmi volbami:

- **Přidat nový úkol** – zadáš název a popis úkolu. Obě pole jsou povinná, program tě upozorní, pokud necháš některé prázdné.
- **Zobrazit všechny úkoly** – vypíše očíslovaný seznam všech aktuálně uložených úkolů.
- **Odstranit úkol** – zadáš číslo úkolu ze seznamu a program ho odstraní. Při neplatném vstupu tě vyzve k opakování.
- **Konec programu** – bezpečně ukončí aplikaci.

Úkoly jsou uloženy v paměti po dobu běhu programu – po ukončení se neuloží do souboru.

---

## Požadavky

- **Python 3.10 nebo novější**

Žádné externí knihovny nejsou potřeba – program používá pouze standardní knihovnu Pythonu.

Verzi Pythonu ověříš příkazem:

```bash
python --version
```

---

## Spuštění

**1. Stáhni nebo naklonuj repozitář:**

```bash
git clone https://github.com/pkrotil95-jpg/Task-manager.git
cd Task-manager
```

**2. Spusť program:**

```bash
python spravce_ukolu.py
```

Po spuštění se zobrazí hlavní menu:

```
Správce úkolů - Hlavní menu
1. Přidat nový úkol
2. Zobrazit všechny úkoly
3. Odstranit úkol
4. Konec programu
Vyberte možnost (1-4):
```

---

## Struktura repozitáře

```
Task-manager/
├── spravce_ukolu.py        # Hlavní soubor programu
├── testovaci_pripady_v3.docx  # Testovací případy (36 TC)
└── README.md
```

---

## Testování

Testovací případy jsou zdokumentovány v souboru `testovaci_pripady_v3.docx`. Dokument obsahuje celkem **42 testovacích případů** rozdělených do čtyř sekcí podle funkcí programu, včetně pozitivních, negativních a hraničních testů s přesným výstupem konzole.
