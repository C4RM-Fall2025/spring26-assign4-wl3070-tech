
def getBondDuration(y, face, couponRate, m, ppy = 1):
    r = y / ppy
    N = m * ppy
    C = face * couponRate / ppy

    price = 0
    weighted_sum = 0

   for t in range(1, N):
        pv = C / (1 + r) ** t
        price = price + pv
        weighted_sum = weighted_sum + t * pv

    cf_last = C + face
    pv_last = cf_last / (1 + r) ** N

    price = price + pv_last
    weighted_sum = weighted_sum + N * pv_last

    duration_periods = weighted_sum / price
    duration_years = duration_periods / ppy

    bondDuration = duration_years

    return(bondDuration)


