class CircularArray:
    def __init__(self, lin, st, sz):
        # Initializing Variables
        self.start = 0
        self.size = 0
        self.cir = []

        # if lin = [10, 20, 30, 40, None]
        # then, CircularArray(lin, 2, 4) will generate
        # cir = [40, null, 10, 20, 30]
        #Todo

        self.start=st
        self.size=sz
        self.cir=[None]*len(lin)
        for i in range(self.size):
            self.cir[st]=lin[i]
            st+=1
            if st==len(lin):
                st=(st)%len(lin)


    # Hints: set the values for initialized variables
    # Print from index 0 to len(cir) - 1
    def printFullLinear(self): #Easy
        # To Do
        for i in range(len(self.cir)):
            if i!=len(self.cir)-1:
                print(self.cir[i],end=", ")
            else:
                print(self.cir[i])


    # Print from start index and total size elements
    def printForward(self): #Easy
        # To Do

        j=self.start
        for i in range(self.size):
            if i!=self.size-1:
                print(self.cir[j],end=", ")
            else:
                print(self.cir[j])
            j=(j+1)%len(self.cir)


    def printBackward(self): #Easy
        # To Do
        last_indx=(self.size+self.start-1)%len(self.cir)
        for i in range(self.size):
            if i!=self.size-1:
                print(self.cir[last_indx],end=", ")
            else:
                print(self.cir[last_indx])
            last_indx-=1
            if last_indx==-1:
                last_indx=len(self.cir)-1


    # With no null cells
    def linearize(self): #Medium
        # To Do
        new_arr, indx=[None]*self.size, self.start
        for i in range(self.size):
            new_arr[i]=self.cir[indx]
            indx=(indx+1)%len(self.cir)
        self.cir=new_arr


    # Do not change the Start index
    def resizeStartUnchanged(self, newcapacity): #Medium
        # To Do
        new_arr, indx =[None]*newcapacity,self.start
        self.linearize()
        for i in range(self.size):
            new_arr[indx]=self.cir[(self.size+i)%len(self.cir)]
            indx=(indx+1)%newcapacity
        self.cir=new_arr


    # This method will check whether the array is palindrome or not
    def palindromeCheck(self): #Hard
        # To Do
        start=self.start
        last=(self.start+self.size-1)%len(self.cir)
        flag=True
        for i in range(self.size//2):
            if self.cir[start]!=self.cir[last]:
                flag=False
                break
            start=(start+1)%len(self.cir)
            last-=1
            if last==-1:
                last=len(self.cir)-1
        print("This array is a palindrome") if flag else print("This array is not a palindrome")


    # This method will sort the values by keeping the start unchanged
    def sort(self):
        # To Do
        for i in range(self.size-1):
            temp=self.start
            for j in range(self.size-1):
                if self.cir[temp%len(self.cir)]>self.cir[(temp+1)%len(self.cir)]:
                    temp2=self.cir[temp%len(self.cir)]
                    self.cir[temp%len(self.cir)]=self.cir[(temp+1)%len(self.cir)]
                    self.cir[(temp+1)%len(self.cir)]=temp2
                temp+=1


    # This method will check the given array across the base array and if they are equivalent interms of values return true, or else return false
    def equivalent(self, cir_arr):
        # To Do
        flag=True
        self.sort()
        cir_arr.sort()
        if self.size!=cir_arr.size:
            return False
        else:
            self.linearize()
            cir_arr.linearize()
            for i in range(self.size):
                if self.cir[i]!=cir_arr.cir[i]:
                    flag=False
                    break
                else:
                    continue
        return flag


    # the method take another circular array and returns a linear array containing the common elements between the two circular arrays.
    def intersection(self, c2):
        # To Do
        if self.size>=c2.size:
            arr=[None]*self.size
        else:
            arr=[None]*c2.size
        k=0
        for i in range(self.size):
            temp=(self.start+i)%len(self.cir)
            for j in range(c2.size):
                temp2=(c2.start+j)%len(c2.cir)
                if self.cir[temp]==c2.cir[temp2]:
                    arr[k]=self.cir[temp]
                    k+=1
        arr2=[None]*k
        for i in range(k):
            arr2[i]=arr[i]
        return arr2