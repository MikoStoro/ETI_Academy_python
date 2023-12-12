
inFile = open('dates.txt', 'r')
outFile = open('datesOut.txt', 'w')
content = inFile.read()
lines = content.split('\n')
years = lines[0].replace('o','0').split(';')
months = lines[1].replace('o','0').split(';')
days = lines[2].replace('o','0').split(';')
names = lines[3].lower().split(';')
names = [ n.capitalize() for n in names ]
for i in range(99):
    name = names[i]
    date = '-'.join([years[i],months[i],days[i]])
    line = "{}: {}\n".format(name,date)
    outFile.write(line)

inFile.close()
outFile.close()

