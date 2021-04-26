import csv
import math

dataSheet = csv.reader(open('D:\Apps\Standert Diviation\data.csv', newline=''))
listData = list(dataSheet)

total = 0

for i in listData:
    total = total + int(i[0])

lenOfListData = len(listData)
mean = total / lenOfListData


squareList=[]
for i in listData:
    a = int(i[0]) - mean
    a = a**2
    squareList.append(a)

totalsq = 0
for i in squareList:
    totalsq += i

totalsq /= lenOfListData
std = math.sqrt(totalsq)

print('Standert Deviation: ', std)