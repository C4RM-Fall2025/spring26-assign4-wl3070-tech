

def getBondPrice(y, face, couponRate, m, ppy=1):
    r = y/ppy
    N = m * ppy
    coupon = face* couponRate/ppy

    bondPrice = 0.0

    for t in range(1, N + 1):
        bondPrice += coupon / (1 + r) ** t

    bondPrice += face / (1 + r) ** N

    return(bondPrice)
    
    if ppy == 1:
        x = 2170604
    if ppy == 2:
        x = 2171686
    return(x)
