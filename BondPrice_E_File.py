

def getBondPrice_E(face, couponRate, yc):
    C = face * couponRate
    N = len(yc)

    bondPrice = 0.0

    t = 1
    for rate in yc:

        if t < N:
            cf = C
        else:
            cf = C + face

        pv = cf / ((1 + rate) ** t)
        bondPrice = bondPrice + pv

        t = t + 1

    return(bondPrice)
    
