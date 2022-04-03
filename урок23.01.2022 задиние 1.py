#x = int(input('Введите размер щаблона:'))
#n = []
#for i in range(x):
    #n.append('_')
#n[0] = '*'
#print(n)
#b = 0
#j = 1
#for i in range(x):
#    if i == x:
#        break
#    n[b] = '_'
 #   b += 1
 #  j += 1
  #  print(n)

n = int(input())
t = ['_'] * n
for h in range(n):
    t[h] = '*'
    if h != 0:
        t[h-1] = '_'
    print(t)

n = int(input())
t = ["_"] * n
for h in range(n,0,-1):
    t[h-1] = '*'
    if h != n:
        t[h] = '_'
    print(t)


    

n = int(input())
t = ['_'] * n
for h in range(n):
    t[n-1-h] = '*'
    t[h] = '*'
    if (h != 0) and (h != n/2):
        t[n-h] = '_'
        t[h-1] = '_'
    print(t)
    

