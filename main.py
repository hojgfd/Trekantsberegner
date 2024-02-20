import mathFuncs

print("Velkommen til min trekantsberegner")
ikkeBeregnet = True
while ikkeBeregnet:

    vinkelType = "damn"
    while vinkelType != "vilkårlig" and vinkelType != "retvinklet":
        vinkelType = input("Skal du beregne en vilkårlig eller retvinklet trekant?").lower()
        if vinkelType == "vilkårlig":
            print("Du valgte vilkårlig")
        elif vinkelType == "retvinklet":
            print("Du valgte retvinklet")
        else:
            print("Forkert valg. Prøv igen")
    sideArray = [1,1,1,1]
    cInvalid = False
    while len(sideArray) > 3 and not cInvalid:
        err = True
        while err:
            #TODO: fix dit lort så den kun accepterer dit valg, når den kan løse resten af trekanten.
            print("Skriv alle dine sidelængder med semikolon mellem hver sidelængde.")
            sideArrInput = input("Start med a. hvis du ikke kender en sidelængde så definer den 0.")

            siderStr = sideArrInput.split(";")
            try:
                sideArray = [float(number) for number in siderStr]
                err = False
            except:
                print("Dine sider kan kun være tal")

        if len(sideArray) > 3:
            print("Du kan ikke have mere end 3 sider i en trekant. Prøv igen.")
        elif sideArray[2] < sideArray[0] or sideArray[2] < sideArray[1]:
            print("c skal være hypotenusen")
            cInvalid = True
        else:
            print("Dine sider er:", sideArray)

    vinkelArray = [1,1,1,1]

    while len(vinkelArray) > 3 or mathFuncs.sumArray(vinkelArray) > 180:
        err = True
        while(err):
            try:
                print("Skriv alle dine vinkler med semikolon mellem hver vinkel.")
                vinkelArrInput = input("Start med A. hvis du ikke kender en vinkler så definer den 0.")
                vinklerStr = vinkelArrInput.split(";")
                vinkelArray = [float(number) for number in vinklerStr]
                err=False
                if len(vinkelArray) > 3 or mathFuncs.sumArray(vinkelArray) > 180:
                    print("Du kan ikke have mere end 3 vinkler i en trekant. Prøv igen.")
                if mathFuncs.sumArray(vinkelArray) > 180:
                    print("Vinkelsummen af en trekant kan ikke være mere end 180. Prøv igen.")
                #TODO: FIX BELOW STATEMENT
                #if(mathFuncs.sumArray(vinkelArray) == 180 and len(vinkelArray) != 3):
                    #print("Dine vinkler må kun være lig med 180 hvis du kender alle tre vinkler. Prøv igen.")
                else:
                    print("Dine vinkler er:", vinkelArray)
            except:
                print("Dine vinkler kan kun være tal")

    if vinkelType == "vilkårlig":
        result = mathFuncs.beregnVilkårlig(sideArray,vinkelArray)
        if(result!=-1):
            print("Sider: ")
            print("Vinkler: ")
            ikkeBeregnet = False
    elif vinkelType == "retvinklet":
        result = mathFuncs.beregnRetvinklet(sideArray, vinkelArray)
        if (result != -1):
            print(str("Sider: " + "\na: " + str(result[0]) + "\nb: " + str(result[1]) + "\nc: " + str(result[2])))
            print("Vinkler: ")
            ikkeBeregnet = False

