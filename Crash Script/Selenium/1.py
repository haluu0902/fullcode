import csv
with open('user.csv','w',newline='') as f:
    writer = csv.writer(f)
    writer.writerow([0, 1, 2])
    writer.writerow(['a', 'b', 'c'])