```python
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
      data.append(row)                                                                               // use the sample code to import my data into the list

for station in station_list:
    for row in data:
        if row['station_id'] == station and row['PRES'] != '-99.000' and row['PRES'] != '-999.000':  // store the target data into my target list except the unwanted data
            target_data[station_list.index(station)].append(float(row['PRES']))
for i in range(5):
    mean = 0
    for j in range(len(target_data[i])):
            mean += target_data[i][j]                                                                // sum all data together
    if len(target_data[i]) == 0:
        answer.append([station_list[i], 'None'])                                                     // if the length = 0, output 'None'
    else:
        answer.append([station_list[i], round((mean / len(target_data[i])), 2)])                     // find the average
 
print(answer)                                                                                        // print out my answer
```
**Following is my result**  
`[['C0A880', 1018.66], ['C0F9A0', 968.52], ['C0G640', 1018.41], ['C0R190', 1012.15], ['C0X260', 1013.19]]`
