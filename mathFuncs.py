import math

def sumArray(array):
    sum = 0
    for i in array:
        sum += i
    return (sum)

def beregnVilkårlig(sider, vinkler):
    try:
        print("Beregner din vilkårlige trekant...")
        #TODO: BEREGN DE SIDSTE SIDER OG VINKLER!



        siderOgVinkler = [sider+vinkler]
        return siderOgVinkler
    except:
        print("Der skete en fejl ved beregningen. Din trekant er sikkert fake. Start forfra.")
        return -1

def beregnRetvinklet(sider, vinkler):
    try:
        print("Beregner din retvinklede trekant...")
        # TODO: BEREGN DE SIDSTE SIDER OG VINKLER!

        for index, side in enumerate(sider):
            if side == 0:
                if index == 0:
                    print("Beregner a...")
                    if sider[1] != 0 and sider[2] != 0:
                        sider[0] = math.sqrt(math.pow(sider[2], 2) - math.pow(sider[1], 2))
                    elif sider[2] != 0 and vinkler[1] != 0:
                        sider[0] = sider[2]*math.cos(vinkler[1])
                    elif sider[2] != 0 and vinkler[0] != 0:
                        sider[0] = sider[2]*math.sin(vinkler[0])
                    elif sider[1] != 0 and vinkler[0] != 0:
                        sider[0] = sider[1]*math.tan(vinkler[0])
                    elif sider[1] != 0 and vinkler[1] != 0:
                        sider[0] = sider[1]/math.tan(vinkler[1])
                    else:
                        print("Kunne ikke beregne a.")
                elif index == 1:
                    print("Beregner b...")
                    if sider[0] != 0 and sider[2] != 0:
                        sider[1] = math.sqrt(math.pow(sider[2], 2) - math.pow(sider[0], 2))
                    else:
                        print("Kunne ikke beregne b.")
                elif index == 2:
                    print("Beregner c...")
                    if sider[0] != 0 and sider[1] != 0:
                        sider[1] = math.sqrt(math.pow(sider[0], 2) + math.pow(sider[1], 2))
                    else:
                        print("Kunne ikke beregne c.")
            else:
                continue

        for index, vinkel in enumerate(vinkler):
            if vinkel == 0:
                if index == 0:
                    print("Beregner A...")

                elif index == 1:
                    print("Beregner B...")

                elif index == 2:
                    print("Beregner C...")
                    vinkler[2] = 90
            else:
                continue

        siderOgVinkler = sider
        return siderOgVinkler
    except:
        print("Der skete en fejl ved beregningen. Din trekant er sikkert fake. Start forfra.")
        return -1
