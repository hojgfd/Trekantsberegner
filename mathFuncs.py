import math

def sumArray(array):
    sum = 0
    for i in array:
        sum += i
    return sum

def beregnVilkårlig(sider, vinkler):
    try:
        print("Beregner din vilkårlige trekant...")
        if sider[0] != 0 and vinkler[0] != 0 and vinkler[1] != 0:
            vinkler[2] = 180-vinkler[0]-vinkler[1]
            sider[1] = (math.sin(vinkler[1]) * sider[0]) / math.sin(vinkler[0])
            sider[2] = (math.sin(vinkler[2]) * sider[0]) / math.sin(vinkler[0])
        elif sider[1] != 0 and vinkler[0] != 0 and vinkler[1] != 0:
            vinkler[2] = 180-vinkler[0]-vinkler[1]
            sider[0] = (math.sin(vinkler[0]) * sider[1]) / math.sin(vinkler[1])
            sider[2] = (math.sin(vinkler[2]) * sider[1]) / math.sin(vinkler[1])
        elif sider[2] != 0 and vinkler[0] != 0 and vinkler[1] != 0:
            vinkler[2] = 180-vinkler[0]-vinkler[1]
            sider[0] = (math.sin(vinkler[0]) * sider[2]) / math.sin(vinkler[2])
            sider[1] = (math.sin(vinkler[1]) * sider[2]) / math.sin(vinkler[2])
        elif sider[0] != 0 and vinkler[0] != 0 and vinkler[2] != 0:
            vinkler[1] = 180 - vinkler[0] - vinkler[2]
            sider[1] = (math.sin(vinkler[1]) * sider[0]) / math.sin(vinkler[0])
            sider[2] = (math.sin(vinkler[2]) * sider[0]) / math.sin(vinkler[0])
        elif sider[1] != 0 and vinkler[0] != 0 and vinkler[2] != 0:
            vinkler[1] = 180 - vinkler[0] - vinkler[2]
            sider[0] = (math.sin(vinkler[0]) * sider[1]) / math.sin(vinkler[1])
            sider[2] = (math.sin(vinkler[2]) * sider[1]) / math.sin(vinkler[1])
        elif sider[2] != 0 and vinkler[0] != 0 and vinkler[2] != 0:
            vinkler[1] = 180 - vinkler[0] - vinkler[2]
            sider[0] = (math.sin(vinkler[0]) * sider[2]) / math.sin(vinkler[2])
            sider[2] = (math.sin(vinkler[1]) * sider[2]) / math.sin(vinkler[2])
        elif sider[0] != 0 and vinkler[1] != 0 and vinkler[2] != 0:
            vinkler[0] = 180 - vinkler[1] - vinkler[2]
            sider[1] = (math.sin(vinkler[1]) * sider[0]) / math.sin(vinkler[0])
            sider[2] = (math.sin(vinkler[2]) * sider[0]) / math.sin(vinkler[0])
        elif sider[1] != 0 and vinkler[1] != 0 and vinkler[2] != 0:
            vinkler[0] = 180 - vinkler[1] - vinkler[2]
            sider[0] = (math.sin(vinkler[0]) * sider[1]) / math.sin(vinkler[1])
            sider[2] = (math.sin(vinkler[2]) * sider[1]) / math.sin(vinkler[1])
        elif sider[2] != 0 and vinkler[1] != 0 and vinkler[2] != 0:
            vinkler[0] = 180 - vinkler[1] - vinkler[2]
            sider[0] = (math.sin(vinkler[0]) * sider[2]) / math.sin(vinkler[2])
            sider[1] = (math.sin(vinkler[1]) * sider[2]) / math.sin(vinkler[2])
        elif sider[0] != 0 and sider[1] != 0 and vinkler[0] != 0:
            vinkler[1] = math.degrees(math.asin((math.sin(vinkler[0])*sider[1])/(sider[0])))
            vinkler[2] = 180 - vinkler[0] - vinkler[1]
            sider[2] = math.sqrt(sider[0]**2 + sider[1]**2 + 2 * sider[0] * sider[1] * math.sin(vinkler[2]))
        elif sider[0] != 0 and sider[1] != 0 and vinkler[1] != 0:
            vinkler[0] = math.degrees(math.asin((math.sin(vinkler[1]) * sider[0]) / sider[1]))
            vinkler[2] = 180 - vinkler[0] - vinkler[1]
            sider[2] = math.sqrt(sider[0] ** 2 + sider[1] ** 2 + 2 * sider[0] * sider[1] * math.sin(vinkler[2]))
        elif sider[0] != 0 and sider[1] != 0 and vinkler[2] != 0:
            vinkler[0] = math.degrees(math.asin((math.sin(vinkler[2]) * sider[0]) / sider[2]))
            vinkler[1] = 180 - vinkler[0] - vinkler[2]
            sider[2] = math.sqrt(sider[0] ** 2 + sider[1] ** 2 - 2 * sider[0] * sider[1] * math.cos(vinkler[2]))
        elif sider[0] != 0 and sider[2] != 0 and vinkler[0] != 0:
            vinkler[2] = math.degrees(math.asin((math.sin(vinkler[0])) * sider[2] / sider[0]))
            vinkler[1] = 180 - vinkler[0] - vinkler[2]
            sider[1] = math.sqrt(sider[0] ** 2 + sider[1] ** 2 - 2 * sider[0] * sider[2] * math.cos(vinkler[1]))
        elif sider[0] != 0 and sider[2] != 0 and vinkler[1] != 0:
            vinkler[0] = math.degrees(math.acos((sider[1]**2+sider[2]**2-sider[0]**2)/(2*sider[1]*sider[2])))
            vinkler[2] = math.degrees(math.acos((sider[0]**2+sider[1]**2-sider[2]**2)/(2*sider[0]*sider[1])))
            sider[1] = math.sqrt(sider[0] ** 2 + sider[2] ** 2 - 2 * sider[0] * sider[2] * math.cos(vinkler[1]))
        elif sider[0] != 0 and sider[2] != 0 and vinkler[2] != 0:
            vinkler[0] = math.degrees((math.asin(vinkler[2]*sider[0])/sider[2]))
            vinkler[1] = 180 - vinkler[0] - vinkler[2]
            sider[1] = (math.sin(vinkler[1])*sider[2])/(math.sin(vinkler[2]))
        elif sider[1] != 0 and sider[2] != 0 and vinkler[0] != 0:
            vinkler[1] = math.degrees((math.asin(math.sin(vinkler[0]) * sider[0]) / sider[0]))
            vinkler[2] = 180 - vinkler[0] - vinkler[1]
            sider[0] = math.sqrt(sider[1]**2+sider[2]**2-2*sider[1]*sider[2])
        elif sider[1] != 0 and sider[2] != 0 and vinkler[1] != 0:
            vinkler[2] = math.degrees((math.asin(math.sin(vinkler[1]) * sider[2]) / sider[1]))
            vinkler[0] = 180 - vinkler[1] - vinkler[2]
            sider[0] = (math.sin(vinkler[0])*sider[1])/math.sin(vinkler[1])
        elif sider[1] != 0 and sider[2] != 0 and vinkler[2] != 0:
            vinkler[1] = math.degrees((math.asin(math.sin(vinkler[2]) * sider[1]) / sider[2]))
            vinkler[0] = 180 - vinkler[1] - vinkler[2]
            sider[0] = (math.sin(vinkler[0])*sider[2])/math.sin(vinkler[2])
        elif sider[0] != 0 and sider[1] != 0 and sider[2] != 0:
            vinkler[0] = math.degrees(math.acos((sider[1]**2+sider[2]**2-sider[0]**2)/(2*sider[1]*sider[2])))
            vinkler[1] = math.degrees(math.acos((sider[0]**2+sider[2]**2-sider[1]**2)/(2*sider[0]*sider[2])))
            vinkler[2] = 180 - vinkler[0]-vinkler[1]
        siderOgVinkler = sider+vinkler
        return siderOgVinkler
    except:
        print("Der skete en fejl ved beregningen.")
        return -1

def beregnRetvinklet(sider, vinkler):
    try:
        print("Beregner din retvinklede trekant...")

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
                    elif sider[0] != 0 and vinkler[0] != 0:
                        sider[1] = sider[0]/math.tan(vinkler[0])
                    elif sider[0] != 0 and vinkler[1] != 0:
                        sider[1]=sider[0]*math.tan(vinkler[1])
                    elif sider[2] != 0 and vinkler[0] != 0:
                        sider[1] = sider[2]*math.cos(vinkler[0])
                    elif sider[2] != 0 and vinkler[1] != 0:
                        sider[1] = sider[2]*math.sin(vinkler[1])
                    else:
                        print("Kunne ikke beregne b.")
                elif index == 2:
                    print("Beregner c...")
                    if sider[0] != 0 and sider[1] != 0:
                        sider[2] = math.sqrt(math.pow(sider[0], 2) + math.pow(sider[1], 2))
                    elif sider[0] != 0 and vinkler[0] != 0:
                        sider[2] = sider[0]/math.sin(vinkler[0])
                    elif sider[0] != 0 and vinkler[1] != 0:
                        sider[2] = sider[0]/math.cos(vinkler[1])
                    elif sider[1] != 0 and vinkler[0] != 0:
                        sider[2] = sider[1]/math.cos(vinkler[0])
                    elif sider[1] != 0 and vinkler[1] != 0:
                        sider[2] = sider[1]/math.sin(vinkler[1])
                    else:
                        print("Kunne ikke beregne c.")
            else:
                continue

        for index, vinkel in enumerate(vinkler):
            if vinkel == 0:
                if index == 0:
                    print("Beregner A...")
                    vinkler[0] = math.degrees(math.atan(sider[0]/sider[1]))
                elif index == 1:
                    print("Beregner B...")
                    vinkler[1] = math.degrees(math.atan(sider[1]/sider[0]))
                elif index == 2:
                    print("Beregner C...")
                    vinkler[2] = 90
            else:
                continue

        siderOgVinkler = sider + vinkler
        return siderOgVinkler
    except:
        print("Der skete en fejl ved beregningen. ")
        return -1
