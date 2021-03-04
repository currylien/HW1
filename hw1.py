import csv

cwb_filename = '108061101.csv'
data = []
target_data = []
for i in range(5): 
    target_data.append([])
station_list = ['C0A880', 'C0F9A0', 'C0G640', 'C0R190', 'C0X260']
answer = []

with open(cwb_filename) as csvfile:
   mycsv = csv.DictReader(csvfile)
   for row in mycsv:
      data.append(row)

for station in station_list:
    for row in data:
        if row['station_id'] == station and row['PRES'] != '-99.000' and row['PRES'] != '-999.000':
            target_data[station_list.index(station)].append(float(row['PRES']))
for i in range(5):
    mean = 0
    for j in range(len(target_data[i])):
            mean += target_data[i][j]
    if len(target_data[i]) == 0:
        answer.append([station_list[i], 'None'])
    else:
        answer.append([station_list[i], round((mean / len(target_data[i])), 2)])

print(answer)
