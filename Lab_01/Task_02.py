#Rotate Left k cells

def rotateLeft(source,r):
    for i in range(r):
        temp=source[0]
        for j in range(len(source)-1):
            source[j]=source[j+1]
        source[len(source)-1]=temp
    return source

source=[10,20,30,40,50,60]
rotateLeft(source,3)