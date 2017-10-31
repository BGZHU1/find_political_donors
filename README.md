# **Find_Political_Donors : **(python 2.7)

## Part one  (source code inside src folder) :

1) **run** :  ./run.sh 



2) **file structure** : 



        a. main file - find_political_donors.py

        b.  using min/max heap for running median calculation : runningMedian.py

        c. calculate the sort by date result - calculateSortByDate.py

        d. write the results : writeToFiles.py



3) **time /space trade off & special considerations** :



        a. for the incoming data stream : for each key pair, create key/objects  mapping to store running results .

        for the running median, using min/max heap for the sorting efficiency 



        b. for sort by date processing : using batch processing at one time



        c. edge cases : missing value, validate value, and also sorting ID / date pairs





## Part Two  (3 tests) :

1) **run** : ./run_tests.sh (in the insight_testsuite folder)



2) **test cases** : one original test case, one tests missing value, one tests the correctness of the output and sorting results.
