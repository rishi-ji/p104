import csv
with open('Height-Weight.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)
file_data.pop(0)
new_data=[]
for i in range(len(file_data)):
	n_num = file_data[i][1]
	new_data.append(float(n_num))


n = len(new_data)
#To Find Mean
'''total =0
for x in new_data:
    total += x

mean = total / n

print("Mean / Average is: " + str(mean))'''
#To find Medium
new_data.sort()



if n % 2 == 0:
	median1 = float(new_data[n//2])
	median2 = float(new_data[n//2 - 1])
	median = (median1 + median2)/2
else:
	median = new_data[n//2]
print("Median is " + str(median))