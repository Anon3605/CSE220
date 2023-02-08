#Shift left k cell:

def shiftLeft(source, r):
    temp=len(source)
    for i in range(r):
        for j in range(temp-1):
            source[j]=source[j+1]
        source[temp-1]=0
        temp-=1
    return source
source=[10,20,30,40,50,60]
print(shiftLeft(source,3))