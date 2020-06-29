import csv

#file path of the file need for the conversion
READ = r'C:\Users\Computer\Desktop\Last_correction.csv'
WRITE = r'C:\Users\Computer\Desktop\test_123.csv'

def csvReader(READ):
    file = open(READ)
    readerValue = csv.reader(file, delimiter=',')
    return readerValue,file

#this algorithm works for any column to get flatten by passing the column number to be flatten

def flattenCSV(readerValue,columnNumber,file):
    listToWrite = []
    getColNum = len(next(readerValue)) # Get count of the total number of column
    file.seek(0)  #To keep the header values
    for row in readerValue:
       flattenColumn = row[columnNumber]
       flattenColumnSplit = list(flattenColumn.split(','))
       leftColumnSet = list(row[0:columnNumber])
       rightColumnSet = list(row[columnNumber+1:getColNum])
       for flattenColumn in flattenColumnSplit:
           if(columnNumber>0 and getColNum != columnNumber):
               desiredColumn = leftColumnSet + [str(flattenColumn)] + rightColumnSet
           elif(columnNumber == getColNum):
               desiredColumn = leftColumnSet + [str(flattenColumn)]
           else:
               desiredColumn = [str(flattenColumn)] + rightColumnSet
           listToWrite.append(desiredColumn)
    return  listToWrite


#csv writer function will write the list of rows to desired list file accordingly
def csvWriter(writeFilePath, writeList):
    with open(writeFilePath, 'w') as file:
        writer = csv.writer(file,quoting= csv.QUOTE_ALL)
        writer.writerows(writeList)

#read csv file
readerValue, file = csvReader(READ)

#Please input the column number to flatten the csv and the index starts from 0 to n column number
desiredList = flattenCSV(readerValue,5,file)
print(desiredList)

#write csv to a new or existing file
writerValue = csvWriter(WRITE,desiredList)
if(writerValue):
    print("Success")

