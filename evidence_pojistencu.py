print("-------------------------\nEvidence pojištěných\n-------------------------")
class Pojistenec:
    def __init__(self, jmeno, prijmeni, telefon, vek):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.telefon = telefon
        self.vek = vek


class Evidence:
    def __init__(self):
        self.pojistenci = []

    def pridat(self, pojistnik):
        self.pojistenci.append(pojistnik)

    def vypis(self):
        for pojistnik in self.pojistenci:
            print(pojistnik.jmeno, pojistnik.prijmeni, pojistnik.telefon, pojistnik.vek)

    def vyhledat(self, jmeno, prijmeni):
        for pojistnik in self.pojistenci:
            if pojistnik.jmeno == jmeno and pojistnik.prijmeni == prijmeni:
                return pojistnik
        return None

evidence = Evidence()

print("Vyber si akci:")
print("1 - Přidej nového pojištěného")
print("2 - Vypsat všechny pojištěné")
print("3 - Vyhledat pojištěného")
print("4 - Konec programu")

while True:

    akce = input()

    if akce == "1":
        jmeno = input("Zadej jméno pojištěného:\n ").capitalize()
        prijmeni = input("Zadej příjmení:\n ").capitalize()
        telefon = input("Zadejte telefonní číslo:\n ")
        vek = input("Zadejte věk:\n ")
        pojistenec = Pojistenec(jmeno, prijmeni, telefon, vek)
        evidence.pridat(pojistenec)
        print("Data byla uložena. Pokračujte libovolnou klávesou...")

    elif akce == "2":
        evidence.vypis()
        print("Pokračujte libovolnou klávesou...")

    elif akce == "3":
        jmeno = input("Zadej jméno pojištěného:\n ").capitalize()
        prijmeni = input("Zadej příjmení:\n ").capitalize()
        pojistnik = evidence.vyhledat(jmeno.capitalize(), prijmeni.capitalize())
        if pojistnik:
            print(pojistnik.jmeno, pojistnik.prijmeni, pojistnik.telefon, pojistnik.vek)
        else:
            print("Pojisteny nebyl nalezen.")
        print("Pokračujte libovolnou klávesou...")

    elif akce == "4":
        break
    else:
        print("Neplatný výběr. Zkuste znovu zadat číslo v rozsahu 1-4.")