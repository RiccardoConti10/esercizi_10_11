parole_totali = []
numero_lettere_totali = []
lettere = 0
while True :
    parola_scelta = input("Inserire la parola (inserire "stop" per fermare) ")
    if parola == "stop" :
        break
    else:
        parole_totali.append (parola_scelta)
for p in parole_totali :
    lettere = len (p)
    numero_lettere_totali.append(lettere)
    lettere = 0 
for i in range (len(parole_totali)) :
    print (parole_totali [i-1], "è di", numero_lettere_totali [i-1], "lettere")
