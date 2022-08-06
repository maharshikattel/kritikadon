from csv import DictReader
# ordered dict

with open("new_file.csv","r") as rf:
    csv_reader = DictReader(rf,delimiter=",")
    for row in csv_reader:
        print(row) #order dict