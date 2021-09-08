goed = input("Is the kaas geel?(y/n) ")
if goed == "y":
    gaten = input("Zitten er gaten in?(y/n) ")
    if gaten == "y":
        duur = input("Is de kaas belachelijk duur?(y/n) ")
        if duur == "y":
            print("Jouw kaas is Emmenthaler")
            exit()
        elif duur == "n":
            print("Jouw kaas is Leerdammer")
            exit()
    elif gaten == "n":
        steen = input("Is de kaas hard als steen?(y/n) ")
        if steen == "y":
            print("Jouw kaas is Pamnigiano reggiano")
            exit()
        elif steen == "n":
            print("Jouw kaas is Goudse kaas")
            exit()
elif goed == "n":
    schimmel = input("Heeft de kaas blauwe schimmels?(y/n) ")
    if schimmel == "y":
        korst = input("Heeft de kaas een korst?(y/n) ")
        if korst == "y":
            print("Jouw kaas is Bleu de Rochbaron")
            exit()
        elif korst == "n":
            print("Jouw kaas is Foume d'Ambert")
            exit()
    elif schimmel == "n":
        korst = input("Heeft de kaas een korst?(y/n) ")
        if korst == "y":
            print("Jouw kaas is Bleu de Camembert")
            exit()
        elif korst == "n":
            print("Jouw kaas is Mozzarella")
            exit()

print('Verkeerde input gebruik "y" en "n"')