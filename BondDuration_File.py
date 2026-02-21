
def getBondDuration(y, face, couponRate, m, ppy = 1):
    r = y / ppy
    N = m * ppy
    C = face * couponRate / ppy

    price = 0
    weighted_sum = 0

    t = 1
    while t <= (N - 1):
        pv = C / ((1 + r) ** t)
        price = price + pv
        weighted_sum = weighted_sum + (t * pv)
        t = t + 1
        
    pv_last = (C + face) / ((1 + r) ** N)
    price = price + pv_last
    weighted_sum = weighted_sum + (N * pv_last)

    duration_periods = weighted_sum / price
    bondDuration = duration_periods / ppy

    return(bondDuration)
