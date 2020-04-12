import json
import csv

with open('E:\\GitHub-respositories\\python-spider\\info.json', encoding='utf-8') as f:
    s = f.readlines()
f.close()

c = open('E:\\GitHub-respositories\\python-spider\\info.csv', 'w', encoding='utf-8', newline='')
csv_writer = csv.writer(c)

for each in s:
    x = json.loads(each)
    temp = []
    for item in x:
        if x[item] == []:
            temp += ['0']
        else:
            temp += x[item]
    csv_writer.writerow(temp)

c.close() 
