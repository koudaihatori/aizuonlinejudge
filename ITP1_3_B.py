
array = []
while True:
  z = input()
  if(int(z)== 0):
    break
  else:
    array.append(z)

a = 1
for i in array:
  print('Case ' + str(a) + ': ' + str(i))
  a += 1


