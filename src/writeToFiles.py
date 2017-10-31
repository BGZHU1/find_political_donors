import os

class writeToFiles(object) :

    def writeFile1(self, record):
        self.writePath = os.getcwd()+"/output"
        self.name1 = "medianvals_by_zip.txt"
        with open(os.path.join(self.writePath,self.name1), "w") as self.file1:
            for i in record :
                self.file1.write(i + '\n')
        self.file1.close()


    def writeFile2(self, record):
        self.writePath = os.getcwd()+"/output"
        self.name2 = "medianvals_by_date.txt"
        with open(os.path.join(self.writePath,self.name2), "w") as self.file2:
            for i in record:
                self.file2.write(i + '\n')
        self.file2.close()
