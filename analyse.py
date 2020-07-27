import pandas as pd

def getSeconds(time):
    return int(time[0])*60*60 + int(time[1])*60 + int(time[2])

sheet = pd.read_excel('test.xlsx', sheet_name='raw(T)', header=1)
data = sheet[['Date','Speed']]

cars = []
row = data.iloc[0]
car = [row['Speed']]

for i in range(1,data.shape[0]):
    row = data.iloc[i]
    date = row['Date']
    speed = row['Speed']
    time = getSeconds(date.split(' ')[1].split(':'))
    prevTime = getSeconds(data.iloc[i-1]['Date'].split(' ')[1].split(':'))
    if (time - prevTime) < 3:
        car.append(speed)
    else:
        cars.append(max(car))
        car = [speed]

cars.append(max(car))

print('num cars =', len(cars))

