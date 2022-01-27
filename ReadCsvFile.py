import csv


class ReadCsvFile:

    def readFromFileMessage(self):
        messageTitleTable = []
        messageTable = []
        counter = 0
        with open("Message.csv", 'r', encoding='utf-8') as file:
            csvReader = csv.reader(file, delimiter=';')
            header = next(csvReader)
            for row in csvReader:
                counter = counter + 1
                messageTitleTable.append(row[0])
                messageTable.append(row[1])
                # print(row)
        return messageTitleTable, messageTable, counter

    def readFromPulseDate(self):
        x = []
        y = []
        with open("PulseDate.csv", 'r') as file:
            csvReader = csv.reader(file, delimiter=';')
            header = next(csvReader)
            for row in csvReader:
                y.append(int(row[0]))
                x.append(row[1])
                # print(row)
        return x,y

    def readFromTemperatureData(self):
        x = []
        y = []

        with open("TemperatureData.csv", 'r') as file:
            csvReader = csv.reader(file, delimiter=';')
            header = next(csvReader)
            for row in csvReader:
                y.append(float(row[0]))
                x.append(row[1])
                # print(row)
        return x, y

    def readFromSaturationData(self):
        x = []
        y = []

        with open("SaturationData.csv", 'r') as file:
            csvReader = csv.reader(file, delimiter=';')
            header = next(csvReader)
            for row in csvReader:
                y.append(float(row[0]))
                x.append(row[1])
                # print(row)
        return x, y