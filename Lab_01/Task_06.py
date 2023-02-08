def removeAll(source,size,element):
  for idx in range(len(source)-1):
      if source[idx] == element:
          source[idx]=0
          i = idx
          while i < size:
              source[i] = source[i + 1]
              i += 1

  for idx in range(len(source)-1):
      if source[idx] == element:
          source[idx] = 0
source=[10,2,30,2,50,60,2,2,0,0]
removeAll(source,7,2)
print(source)