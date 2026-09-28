def recepte(receptes_numurs):
    if receptes_numurs == "1":
        izmaksas = cukura_cena*aboli_kg*0.3
    else:
        izmaksas = cukura_cena*aboli_kg*0.5
    return izmaksas
receptes_numurs=input("Ievadiet receptes numuru: \n1) 1 kg ābolu = 300 gr. cukura\n2) 1 kg ābolu = 500 gr. cukura\n  ")
cukura_cena=float(input("Ievadi cukura cenu: "))
aboli_kg = float(input("Ievadi, cik ābolu tev ir (kg): "))

recepte(receptes_numurs)
print(f"Par cukuru tu samaksāsi {izmaksas} eiro")
