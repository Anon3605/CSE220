def elementRepeat(source):
    dictA ={}
    for i in range(0,len(source)):
        if source[i] not in dictA:
            dictA[source[i]] = 1
        else:
            dictA[source[i]] += 1
    magnitutde = dictA.values()
    for i in dictA.values():
        if i >2 and i in magnitutde:
            return True
        else:
            return False

source = [4,5,6,6,4,3,6,4]
print(elementRepeat(source))