#Shift Right k Cells

def shiftRight(source,r):
    temp=-1
    for i in range(r):
        for j in range(len(source)-1,temp,-1):
            source[j]=source[j-1]
        source[temp+1]=0
        temp+=1
    return source

source=[10,20,30,40,50,60]
shiftRight(source,3)