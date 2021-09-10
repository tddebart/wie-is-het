goed = input("Is the kaas geel?(y/n) ").lower()
if goed == "y":
    gaten = input("Zitten er gaten in?(y/n) ").lower()
    if gaten == "y":
        duur = input("Is de kaas belachelijk duur?(y/n) ").lower()
        if duur == "y":
            print("Jouw kaas is Emmenthaler")
            exit()
        elif duur == "n":
            print("Jouw kaas is Leerdammer")
            exit()
    elif gaten == "n":
        steen = input("Is de kaas hard als steen?(y/n) ").lower()
        if steen == "y":
            print("Jouw kaas is Pamnigiano reggiano")
            exit()
        elif steen == "n":
            print("Jouw kaas is Goudse kaas")
            exit()
elif goed == "n":
    schimmel = input("Heeft de kaas blauwe schimmels?(y/n) ").lower()
    if schimmel == "y":
        korst = input("Heeft de kaas een korst?(y/n) ").lower()
        if korst == "y":
            print("Jouw kaas is Bleu de Rochbaron")
            exit()
        elif korst == "n":
            print("Jouw kaas is Foume d'Ambert")
            exit()
    elif schimmel == "n":
        korst = input("Heeft de kaas een korst?(y/n) ").lower()
        if korst == "y":
            print("Jouw kaas is Bleu de Camembert")
            exit()
        elif korst == "n":
            print("Jouw kaas is Mozzarella")
            exit()

print('Verkeerde input gebruik "y" en "n"')