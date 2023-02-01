def achat():
        payement =float (input("payement : 1 comptent |  2 credit ? "))
        prix = float(input("Prix du bien ? "))
        options =float(input("options suplem ? "))
        Frais =float(input("Frais instal ? "))
        transport =float(input("transport ? "))
        reduc =int(input("reduction ? 1 % | 2 valeur "))
        if (reduc==1):
            reducPrct = float(input("reduction en % ? "))
            reduction = (prix + options) *((100-reducPrct)/100)
        if (reduc ==2):
            reduction = float(input("reduction en Valeur ? "))
        
        acompte =float (input("acompte verse ? "))
        tva=float(input("tva en % ? "))
        
        
        prixImmo = (prix + options + Frais + transport - reduction)
        print("DEBEUG PRIX IMMO = " , prixImmo)
        tvaDeductible = (prixImmo * (tva/100))
        
        print("______RESULTATS______")
        
        print("|Immo / ou autres : " , prixImmo)
        print("|Tva deductible : " , tvaDeductible)
        if acompte != 0 : print ("|Avance acompte versé sur immo : " , acompte)
        
        #voire comment on enregistre quand cest un achat au comptant 
        if payement == 1 :
            print("|Banque: VOIR COUR " ,(prixImmo + tvaDeductible - acompte) )
        if payement == 2 :
            print("|Dette fournisseur : " , (prixImmo + tvaDeductible - acompte))


#CE QUI SERT DE MAIN
choix =float(input("1 achat | 2 vente | 3 ammort "))
if choix == 1: 
    achat()
if choix == 2:
    #vente()
    print("PAS ENCORE CODE")

if choix == 3:
    #ammortissement()
    print("PAS ENCORE CODE")