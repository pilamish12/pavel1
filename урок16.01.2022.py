time = ['1:47:09', '5:15:10', '5:20:35','1:47:37']
#b = time[0].split(':')
n = []
j = []
for i in time:
    b = i.split(':')
    n.append(b)
rezeld = []
for x in n:
    for d in x:
        d = int(d)
        j.append(d)
    rezeld.append(j)
    j = []
hours = 0
minutes = 0
seconds = 0
for g in rezeld:
    hours += g[0]
    minutes += g[1]
    seconds += g[2]
    if minutes >= 60:
        hours = hours + minutes // 60
        minutes = minutes % 60
    if seconds >= 60:
        minutes = minutes + seconds // 60
        seconds = seconds % 60
print(hours)
print(minutes)
print(seconds)
    


        

        
