area = input ("che area vuoi calcolare? Quella di un quadrato, di un rettangolo, di triangolo o di un cerchio?")
if area == "quadrato":
    lato = int (input ("quanto misura il lato?"))
    print ("l'area è", lato**2)
elif area == "rettangolo" or area == "triangolo" :
    base = int (input ("quanto misura la base?"))
    altezza = int (input ("quanto misura l'altezza?"))
if area == "rettangolo" :
        print ("l'area è", base*altezza)
elif :
        print ("l'area è", base*altezza/2)
elif :
    raggio = int (input ("quant'è il raggio?"))
    print ("l'area è", raggio**2*3,14)
