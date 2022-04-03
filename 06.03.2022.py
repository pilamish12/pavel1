#def x(c):
 #   if c < 0:
  #      return c 
   # else:
    #    c = c * -1
     #   print(c)
#v = int(input())
#x(v)

##   v = []
  #  for i in range(c, b):
   #     v.append(i)
    #v.append(b)
    #print(v)
#x(1, 4)
        
#def is_div(x, y, z):
 #   b = "True"
  #  n = "False"
   # if (x % y == 0) and (x % z == 0):
    #    print(b)
   # else:
    #    print(n)
#is_div(x=4, y=2, z=3)
#def x(c):
    #v = 0
    #b = 0
#    for i in c:
 #       v += i
  #      b += 1
   # v = v / b
   # return v
#c = [1, 2, 3, 5]
#print(x(c))


#def repeat_str(c, b):
 #   return b * c        
#print(repeat_str(5, 'a'))
        
#def x(c):
 #   a = c[0]
  #  for i in c:
   #     if i < a:
    #        a = i
    #return a
#print(x([34, 15, 88, 2]))

#def bool_to_word(c):
 #   if c == True:
  #      return "YES"
   # elif c == False:
    #    return "NO"
#print(bool_to_word(True))
##########################################################################
##########################################################################
##########################################################################

#def summa(x, y):
 #   a = 0  
  #  for i in x:
   #     a +=i
   # for i in y:
    #    a += i
#    return a
#print(summa([10, 10, 10], [10, 10, 10]))

#x = int(input())
#if x < 1000:
  #  a = x // 100
   # if x % 100 == 0:
    #    print(a)
#    else:
 #       b = a + 1
  #      print(b)
#else:
 #   a = x // 100
  #  if x % 100 == 0:
   #     print(a)
   # else:
    #    b = a + 1
         
     #   print(b)

####################################################################
####################################################################

#def update_light(x):
 #   if x == 'green':
  #      return 'yellow'
  #  elif x == 'yellow':
   #     return 'red'
   # else:
    #    return 'green'
#print(update_light('red'))


#def x(a, b, c):
 #   if a > b:
  #      return 0
   # v = b + 1
 #   x = 0
  #  for i in range(a, v, c):
   #     x += i
    #   return x
#print(x(16, 15, 3))

#ban_words = ["hello", "world", "strange"]
#def word_filter(word):
 #   v = []
  #  for i in word:
   #     for o in ban_words:
    #        if i == o:
     #           break
      #  else:
      #      v.append(i)
   # return v
              
#print(word_filter(["hello", "wld", "der"]))


#def generete_shape(x):
 #   if x == 0:
  #    return ''
   # else:
    #    for i in range(x):
     #       v = []
      #      v.append(+)
    
#print(generete_shape(3

def build_roof(r, rc):
    """
    input: r - data for build roof, rc - data for roof color
    return: bool
    """
    return True

def build_walls(r, wc):
    return True

def build_door(r, dc):
    return True

def build_house(my_dream, colors):
    house = False
    roof_color = colors[0] # 'red'
    house_color = colors[1] # 'white'
    door_color = colors[2] # 'blue'
    roof = my_dream[0] # 'roof'
    walls = my_dream[1] # 'walls'
    
    while house == False:
        roof_status = build_roof(roof, roof_color) # 'roof' 'red'
        walls_status = build_walls(walls, house_color) # 'walls' 'white'
        door_status = build_door(door_color, door_color) # 'blue' 'blue'
        if roof_status == True and walls_status == True and door_status == True:
            house = True
            print('Поздравляю вы построили дом своей мечты!')
    return house
idea = ('roof', 'walls')
colors = ('red', 'white', 'blue')
build_house(idea, colors)








    

   
