#Python version - Python 2.7

 The file I wrote has two parts :

1. Part one is in the source code inside the src folder
Two files :
1) find_political_donors.py for major processing
2) functions.py for calculation functions
run :./run.sh to run the src

2. Part two is the two additional tests I wrote :
1) test two is for the missing value, data validation test
2) test three tests the correctness of output: the running median and the sorting by ID and then by date

run :./run_tests.sh (in the insight_testsuite folder)

3.
1) for processing the medianvals_by_zip result : I store it in dictionary.
key : CMTE_ID + ZIP_CODE
value : list which adding the TRANSACTION_AMT each time the new record come in

2) for processing the medianvals_by_date result : I store it in dictionary.
key : CMTE_ID + TRANSACTION_AMT
value : list which adding the TRANSACTION_AMT
calculate once in the end
In order to sort CMTE_ID and TRANSACTION_AMT, I first make the key value an dictionary,
then reconstruct the pairs using the sorted key pair
