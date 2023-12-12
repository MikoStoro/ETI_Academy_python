import calendar
import random

years = []
days = []
months = []
names = []
nameList = open('imiona.csv', 'r')
nameList = nameList.readlines()
nameList = [ x.split(',')[0] for x in nameList[1:101] ]

with open('dates.txt','w') as file:
    for i in range(100):
        year = random.randrange(1950, 2023)
        month =random.randrange(1,13)
        num_days = calendar.monthrange(year, month)[1]
        year = str(year).replace('0', 'o')
        month =  str(month).replace('0', 'o')
        day = str(random.randrange(1,num_days+1)).replace('0', 'o')
        
        years.append(year)
        days.append(day)
        months.append(month)
        cas  =[str.upper, str.lower]
        name = random.choice(nameList)
        names.append(  ''.join(random.choice(cas)(c) for c in name))
    
    line1 = ';'.join(years) + '\n'
    line2 = ';'.join(months) + '\n'
    line3 = ';'.join(days) + '\n'
    line4 = ';'.join(names) + '\n'
    file.writelines([line1,line2,line3,line4])
    