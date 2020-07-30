import pandas as pd

def getSeconds(time):
    return int(time[0])*60*60 + int(time[1])*60 + int(time[2])

excel = input('Please enter all the file paths for one month separated by a comma and a space (for example for two files put "C:\\Users\\Documents\\file1, C:\\Users\\Documents\\file1,". For one file just put the file path):\n ')
files = excel.split(', ')

full = pd.DataFrame(columns=['Average and Maximum speed', 'Date', 'Speed', 'Evaluation direction'])
for f in files:
    sheet = pd.read_excel(f, sheet_name='raw(T)', header=1)
    full = full.append(sheet, ignore_index=True)

#print(full)

data = full[['Date','Speed']]

cars = []
row = data.iloc[0]
car = [row['Speed']]
month = row['Date'].split(' ')[0][3:]

for i in range(1,data.shape[0]):
    row = data.iloc[i]
    date = row['Date']
    speed = row['Speed']
    time = getSeconds(date.split(' ')[1].split(':'))
    prevTime = getSeconds(data.iloc[i-1]['Date'].split(' ')[1].split(':'))
    if (time - prevTime) < 4:
        car.append(speed)
    else:
        cars.append(max(car))
        car = [speed]

cars.append(max(car))

print('')
print(cars)
print('num cars =', len(cars))
print('Average speed =', sum(cars)/len(cars))
print('Total over 20 =', len([i for i in cars if i > 20 and i <= 30]))
print('Total over 30 =', len([i for i in cars if i > 30 and i <= 40]))
print('Total over 40 =', len([i for i in cars if i > 40 and i <= 50]))
print('Total over 50 =', len([i for i in cars if i > 50]))
print('Max speed =', max(cars))

numCars = len(cars)
aveSpeed = sum(cars)/len(cars)
over20 = len([i for i in cars if i > 20 and i <= 30])
over30 = len([i for i in cars if i > 30 and i <= 40])
over40 = len([i for i in cars if i > 40 and i <= 50])
over50 = len([i for i in cars if i > 50])
maxSpeed = max(cars)
d = {'Number of cars':numCars,'Average Speed':aveSpeed,'Total over 20 and less than 30':over20,'Total over 30 and less than 40':over30,'Total over 40 and less than 50':over40,'Total over 50':over50,'Max speed in the month':maxSpeed}
data = pd.DataFrame(data=d, index=[month])
print(data, '\n')

out = None
try:
    out = pd.read_excel('out.xlsx', index_col=0)
    print(out, '\n')
    out = out.append(data)
    print(out, '\n')
    out.to_excel('out.xlsx')
except FileNotFoundError:
    data.to_excel('out.xlsx')

input('All done, written to out.xlsx. Press Enter to quit')

