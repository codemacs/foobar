__author__ = 'lookmayank'
def checkValid(M,F):
    valid = True
    if (M == F and M != 1):
        valid = False
    elif (M == 0 or F == 0):
        valid = False
    return valid

def answer(M, F):
    numM = int(M)
    numF = int(F)
    count = 0
    while (checkValid(numM,numF)):
        if (numM > numF ):
            if (numF == 1):
                count += (numM -1)
                numM = 1
                break
            quoM = int(numM/numF)
            numM = numM - (numF * quoM )
            count += quoM
        else:
            if (numM == 1 ):
                count += (numF -1)
                numF = 1
                break 
            quoF = int(numF/numM)
            numF = numF - (numM * quoF)
            count += quoF
    if (numM == 1 and numF == 1 ):
        return (str(count))
    else:
        return "impossible"
