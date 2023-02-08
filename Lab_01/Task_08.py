def array_series(n):
  array =[0]*(n*n)
  elements=0
  while elements <=((n*n)-1):
    for i in range(n):
       for j in range(n-(i+1)):
         array[elements] = 0
         elements+=1
       for j in range(i+1,0,-1):
        array[elements]=j
        elements+=1
  return array
num = int(input())
print(array_series(num))