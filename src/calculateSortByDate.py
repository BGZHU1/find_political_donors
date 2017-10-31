from collections import OrderedDict
from decimal import Decimal, ROUND_HALF_UP

class calculateSortByDate (object) :
    #break the original key, reformat date, then reconstruct the sorted dictionary
    def sortDic(self, dic):
        self.newDic = {}
        for self.key in dic :
            self.newPair = self.key.split('|')
            self.newKey = self.newPair[0] + '|' + self.newPair[1][4:] + self.newPair[1][0:4]
            self.newDic[self.newKey] = self.newPair

        self.sortedKeyPair = OrderedDict(sorted(self.newDic.items(), key=lambda v: v[::-1]))
        #print(sortedKeyPair)
        #reConstructDic = defaultdict(list)
        self.reConstructList = []
        for self.i in self.sortedKeyPair :
            self.k = self.sortedKeyPair[self.i]
            self.k = self.k[0]+ '|' + self.k[1]
            self.v = dic[self.k]
            self.li = []
            self.li.append(self.k)
            self.li.append(self.v)
            self.reConstructList.append(self.li)

        return self.reConstructList

    def calculateSortByDate(self, dic):
        self.dic2 = self.sortDic(dic)
        self.record2 = []
        for self.element in self.dic2 :
            self.key = self.element[0]
            self.curRecord = self.element[1]
            self.fixedMedian = int(self.median(self.curRecord))
            self.countNum = len(self.curRecord)
            self.totalNum = int(sum(self.curRecord))
            self.record = self.key + '|' + str(self.fixedMedian) + '|' + str(self.countNum) + '|' + str(self.totalNum)
            self.record2.append(self.record)
        return self.record2


    def median(self, lst):
        self.sortedLst = sorted(lst)
        self.lstLen = len(lst)
        self.index = (self.lstLen - 1) // 2

        if (self.lstLen % 2):
            return Decimal(self.sortedLst[self.index]).quantize(0, ROUND_HALF_UP)
        else:
            return Decimal((float(self.sortedLst[self.index]) + float(self.sortedLst[self.index + 1]))/2.0).quantize(0, ROUND_HALF_UP)
