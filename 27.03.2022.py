#a = int(input("Под какой процент вы кладете деньги:"))
#b = int(input("Сколько вы хотите положить денег в банк:"))
#c = int(input("На сколько лет вы хотите положить деньги в банк:"))
#x = 0
#for i in range(c):
    #b =  b + (b // 100 * 2)
    #x += 1          
    #print(f'Год {x}. На вашем счету {b}')
#print(f'Ваш итоговый счет в банке: {b}')

savings = int(input("Сколько вы хотите положить денег в банк: "))
interest = int(input("Под какой процент вы кладете деньги: ")) / 100
time = int(input("На сколько лет вы хотите положить деньги в банк: "))

def calc_savings(savings, interest, time):
    for t in range(time):
        savings += savings * interest
    return savings

def bank(s, i=0.02, t=1):
    if i > 0.05:
        print('Максимальный процент в нашем банке 5% годовых')        
    else:
        savings = calc_savings(s, i, t)
        return savings
    
total_savings = bank(savings, interest, time)
if total_savings:
    print(f'Ваш итоговый счет в банке: {total_savings}')
    
