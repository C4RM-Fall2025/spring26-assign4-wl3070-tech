

def FizzBuzz(start, finish):
    v = []

    for n in range(start, finish + 1):  
        if (n % 3 == 0) and (n % 5 == 0):
            v.append('fizzbuzz')
        elif n % 3 == 0:
            v.append('fizz')
        elif n % 5 == 0:
            v.append('buzz')
        else:
            v.append(n)

    return(v)


