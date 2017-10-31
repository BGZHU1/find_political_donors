import os
from collections import defaultdict
import datetime

from writeToFiles import *
from runningMedian import *
from calculateSortByDate import *

hashMap_runningMedian = {} #map the dicKey with the heap object
hashMap_totalSum = {} #map the dicKey with the sumObject
hashMap_countRecord = {} #map the dicKey with the countObject

class main(object) :

    def validate_date(self, d):
        self.month = int(d[0:2])
        self.day = int(d[2:4])
        self.year = int(d[4:])
        self.curYear = int(datetime.datetime.now().year)
        if (self.month >= 1 and self.month <= 12 and self.day >=1 and self.day <= 31 and self.year >= 2015 and self.year <= self.curYear) :
            return True
        return False


    def processFiles(self) :
        self.readPath = os.getcwd() +"/input"
        with open(os.path.join(self.readPath,"itcont.txt")) as self.ins:
            #self.dic = defaultdict(list)
            self.dic = []
            self.dic2 = defaultdict(list)
            self.record1 = []

            for self.line in self.ins:
                self.fields = self.line.split("|")
                self.CMTE_ID = self.fields[0]
                self.ZIP_CODE = self.fields[10][0:5]
                self.TRANSACTION_DT = self.fields[13]
                self.TRANSACTION_AMT = self.fields[14]
                self.OTHER_ID = self.fields[15]

                if (len(self.OTHER_ID) != 0 or len(self.CMTE_ID) == 0 or len(self.TRANSACTION_AMT) == 0) :
                    continue

                if (len(self.ZIP_CODE) >= 5) :
                    self.dicKey =  self.CMTE_ID + '|' + self.ZIP_CODE;

              #create object for runningMedian and totalSum for each CMTE_ID + ZIPCODE
                    if self.dicKey not in self.dic :
                        self.findM = runningMedian()
                        hashMap_runningMedian[self.dicKey] = self.findM
                        hashMap_totalSum[self.dicKey] = 0
                        hashMap_countRecord[self.dicKey] = 0
                        self.dic.append(self.dicKey)

               #create object for total sum for each CMTE_ID + ZIPCODE

               #keep a list of running number, get total number of record
                    self.countNum = hashMap_countRecord[self.dicKey] + 1
                    hashMap_countRecord[self.dicKey] = self.countNum

              #get running median
                    self.minMaxHeapObject = hashMap_runningMedian[self.dicKey]
                    self.addElementToHeap = self.minMaxHeapObject.addNum(float(self.TRANSACTION_AMT))
                    self.runningMedian = int(self.minMaxHeapObject.findMedian())

             #get running totalSum
                    self.totalNum = hashMap_totalSum[self.dicKey] + int(self.TRANSACTION_AMT)
                    hashMap_totalSum[self.dicKey] = self.totalNum
                    #self.totalNum = int(sum(self.curDic))

                    self.record1.append(self.dicKey + '|' + str(self.runningMedian) + '|' + str(self.countNum) + '|' + str(self.totalNum))

                if (len(self.TRANSACTION_DT) == 8 and self.validate_date(self.TRANSACTION_DT)) :
                    self.dicKey2 =  self.CMTE_ID + '|' + self.TRANSACTION_DT;
                    self.curDic2 = self.dic2[self.dicKey2]
                    self.curDic2.append(float(self.TRANSACTION_AMT))

            self.calcuation = calculateSortByDate()
            self.record2 = self.calcuation.calculateSortByDate(self.dic2)
            self.writeFiles = writeToFiles()
            self.writeFiles.writeFile2(self.record2)
            self.writeFiles.writeFile1(self.record1)


if __name__ == '__main__':
    objectMain = main()
    objectMain.processFiles()
