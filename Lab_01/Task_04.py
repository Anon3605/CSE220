#Rotate Right k cells

def rotateRight(source,r):
    for i in range(r):
        temp=source[len(source)-1]
        for i in range(len(source)-1,-1,-1):
            source[i]=source[i-1]
        source[0]=temp
    return source

source=[10,20,30,40,50,60]
rotateRight(source,3)