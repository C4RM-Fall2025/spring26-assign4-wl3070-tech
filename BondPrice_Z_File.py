

def getBondPrice_Z(face, couponRate, times, yc):
    coupon = face * couponRate
    n = len(times)

    bondPrice = 0.0

    i = 0
    while i < n:
        t = times[i]     
        r = yc[i]         

        cf = coupon
        if i == n - 1:    
            cf = cf + face

        pv = 1.0 / ((1.0 + r) ** t)
        pvcf = cf * pv

        bondPrice = bondPrice + pvcf
        i = i + 1

    return(bondPrice)
    
