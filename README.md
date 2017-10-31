# **Find_Political_Donors : **(python 2.7)

## Part one  (source code inside src folder) :

1) **run** :  ./run.sh 



2) **source files** : 



        a. main file - find_political_donors.py

        b.  using min/max heap for running median calculation : runningMedian.py

        c. calculate the sort by date result - calculateSortByDate.py

        d. write the results : writeToFiles.py



3) **time /space trade off & special considerations** :



        a. for the incoming data stream : 
        
        I.for each key (CMTE_ID + ZIPCODE) :
        
          * create key/objects mapping to store running median results (running median is calculated using a               seperate class).
          
          * create key/value mapping in dictionay (hashMap) for the running total, running count record

        II. for the running median, using min/max heap for the sorting efficiency 
        

        b. for sort by date processing :
        
        I. for each key (CMTE_ID + Date) :
            
           * using batch processing at one time, store all the key/list in a dictionry,
            where the list contains all the dollar acount for that transaction.

        II. sorting the value first based on CMTE_ID, then the given date :
            * first construct a new dictionary to sort CMTE_ID and date
            * reconstruct the new maaping with original list value
            * since the date is month/day/year, when sorting, reformat it to year/month/day, 
            and change it back after sorting 
        
        
        c. edge cases : missing value, malformat value, same date in different year, repeatitive value, 
                       missing different fields
        
       





## Part Two  (3 tests) :

1) **run** : ./run_tests.sh (in the insight_testsuite folder)



2) **test cases** : one original test case, one tests missing value, malformat value, one tests the correctness of the output and sorting results.
