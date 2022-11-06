import csv
import statistics
filename = open("C:/Users/aniru/Downloads/TAMU.csv", 'r')

file = csv.DictReader(filename)

first = []
last = []
designation = []
h_index_str = []
full = []

for col in file:
    first.append(col['First Name']) 
    last.append(col['Last Name'])
    designation.append(col['Designation'])
    h_index_str.append(col['h-index'])

#h_index to integer
h_index = []
for item in h_index_str:
    h_index.append(int(item))
#print(h_index)
    
full.append(first)
full.append(last)
full.append(designation)
full.append(h_index)
#print(full)

"""
for item in designation:
    count += 1
    if item == user:
        des_index.append(count)
        if type == "Mean":
            sum = 0
            for num in range(0, len(des_index)):
                sum = sum + h_index[num]
        print(sum/len(des_index))
        elif type == "Median":
            med = h_index[des_index[0]:des_index[-1]]
            #print(statistics.median(h_index[des_index[0:-1]]))
        print(med)
        else:
            print("Misinput")
"""        
        
user = input("Enter which designation you would like data for: ")
type = input("Mean or Median: ")
des_index = []
count = -1
if type == "Mean":
    for item in designation:
        count += 1
        if item == user:
            des_index.append(count)
    sum = 0
    for num in range(des_index[0], (des_index[-1] +1)):
        sum = sum + h_index[num]
    print(sum/len(des_index))
elif type == "Median":
    for item in designation:
        count += 1
        if item == user:
            des_index.append(count)
            med = h_index[des_index[0]:des_index[-1]]
    print(statistics.median(h_index[des_index[0]:des_index[-1]]))
else:
    print("Misinput")
