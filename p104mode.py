from collections import Counter
import csv

with open('Height-Weight.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)

new_data=[]
for i in range(len(file_data)):
	n_num = file_data[i][1]
	new_data.append(n_num)



data = Counter(new_data)
mode-data = {
                "50-60": 0,
                "60-70": 0,
                "70-80": 0
            }
for height, occurence in data.items():
    if 50 < float(height) < 60:
        mode-data["50-60"] += occurence
    elif 60 < float(height) < 70:
        mode-data["60-70"] += occurence
    elif 70 < float(height) < 80:
        mode-data["70-80"] += occurence

mode-range, mode-occurence = 0, 0
for range, occurence in mode-data.items():
    if occurence > mode-occurence:
        mode-range, mode-occurence = [int(range.split("-")[0]), int(range.split("-")[1])], occurence
mode = float((mode-range[0] + mode-range[1]) / 2)
print(f"Mode is -> {mode:2f}")