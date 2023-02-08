#Remove an element from an array

def remove(source,size,indx):
    for i in range(indx,size-1):
        source[i]=source[i+1]
    source[size-1]=0
    return source

source=[10,20,30,40,50,0,0]
remove(source,5,2)