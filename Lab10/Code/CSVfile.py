'''
Handling csv files.

Author: Nicoline Louise Thomsen
'''

import csv
import matplotlib.pyplot as plt


class CSVfile:
    def __init__(self):

        self.time = []
        self.lat = []
        self.lon = []


    def loadCSV(self, filename):
        
        with open(filename + '.csv','r') as csvfileQuick:
            plots = csv.reader(csvfileQuick, delimiter=',')
            next(plots)
            for row in plots:
                self.time.append(float(row[0]))
                self.lat.append(float(row[1]))
                self.lon.append(float(row[2]))


    def createCSV(self, filename, headers = []):

        newfile = open(filename + '.csv', 'w+', newline='')  # w+ mode truncates (clears) the file (new file for every test)   
        
        self.logger = csv.writer(newfile, dialect = 'excel')
        if headers:
            self.logger.writerow(headers)

    # Write row to .csv file
    def writeCSV_one(self, data):
        self.logger.writerow(data)

    # Write array to .csv file
    def writeCSV_all(self, data):
        self.logger.writerows(data)


    def plotCSV(self):

        plt.plot(self.lat, self.lon, label = 'Position')
        plt.xlabel('Lattitude')
        plt.ylabel('Longitude')
        plt.title('GNSS Position')
        plt.legend()
        plt.axis('equal')
        plt.show()



if __name__ == '__main__':

    track = CSVfile()
    track.loadCSV('../logs/data_103923')

    newTrack = CSVfile()
    newTrack.createCSV('generated_files/CVS_test', ['Time', 'Latitude', 'Longitude'])
    newTrack.writeCSV_all([[3141, 13413, 643], [543, 5275, 42], [777, 6534, 87]])
    newTrack.writeCSV_one([543, 5275, 42])
    newTrack.writeCSV_one([777, 6534, 87])
