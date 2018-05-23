import csv
f = open('읍면동연령별.csv')

data = csv.reader(f)
next(data)
next(data)
data = list(data)
pivot = []

name = input('궁금한 지역 이름을 입력해주세요 : ')

for row in data :
    if name in row[0] :
        for i in range(3,len(row)) : 
            pivot.append(int(row[i])/int(row[2]))
        break
mn = 1

for row in data :
    s = 0
    for i in range(3, len(row)) :
        row[i] = int(row[i])/int(row[2])
        tmp = (row[i] - pivot[i-3]) ** 2
        s = s + tmp
    if s < mn and (name not in row[0]) :
        result = []
        for i in range(3, len(row)) :
            result.append(row[i])
        mn = s            
        result_name = row[0]
            
import matplotlib.pyplot as plt
plt.rc('font', family = 'Malgun Gothic')
plt.plot(pivot, label = name)
plt.plot(result, label = result_name)
plt.legend()
plt.show()
