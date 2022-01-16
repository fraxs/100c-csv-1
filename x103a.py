#!python3
import csv
"""
Create a function called getData()
getData takes no input parameters
return: file contents as a string

"""
def getData():
    file = open('data.csv')
    csvreader = csv.reader(file)
    header = []
    header = next(csvreader)
    header = ''.join(header)
    rows = []
    for row in csvreader:
        rows.append(row)
    rows = header.join(rows)
    list1 = [header,rows]
    return list1
def main():
    data = getData()
    assert ("list" in str(type(data)))
    assert ("list" in str(type(data[0])))
    assert ("Placed in Service" in data[0]) == True
    assert ("MAC 6c299551c1b5" in data[33]) == True    
    assert data.find("No.,Equipment Item N") == 0
    assert data.find("Barry") == 27089

if __name__ == "__main__":
    main()

