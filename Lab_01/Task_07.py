def array_splitter(source):
    left_sum=0
    right_sum=0
    flag=True
    for i in range(0,len(source)):
        left_sum+=source[i]
    for j in range(0,len(source)):
        left_sum-=source[j]
        right_sum+=source[j]
        if left_sum==right_sum:
            flag=True
            break
        else:
            flag=False
    return (flag)

source=[2, 1, 1, 2, 1]
print(array_splitter(source))