# ---------------------------------------------------------------------------------------------------
# A short program to parse the JMeter CSV result file to print out the average response time and the
# average requests/second for each transaction
#
# note:
# 1) Data structure:
# The simple dictionary data structure was used to store transaction(txn) name as the key (unique)
# and the values of each txn was map as a mutable list where first element of list was to store the
# accumulated transaction count/txn and second element of list was to store the accumulated elapse
# times/txn. An example --> {UT_FeaturedOffer, [25, 54]}. The elements in list per transaction can
# grow to accommodate other information required in future.
# This work was done in `process_results` method
#
# 2) Rationales to obtain the Average RT and the Average requests/second:
# Both metrics were calculated by populating(iterating) the simple transaction based dictionary
# - Average RT per transaction = Total accumulated time / Total accumulated transaction count
# - Average requests/second (tps) = Total accumulated transaction count / length of the execution(sec)
# This work was done in `print_results` method
#
# 3) The output showing the rounding to one decimal digit
# ----------------------------------------------------------------------------------------------------

import csv
import sys
from collections import defaultdict


def print_results(txn_dict, length_millisec):
    """
    Print out the average response time and average transaction per second from the transaction name
    based dictionary
    """
    print("Transaction\tAverage_RT(ms)\tAverage_TPS")
    for txn_name in txn_dict:
        txn_cnt = txn_dict[txn_name][0]
        txn_total_time = txn_dict[txn_name][1]
        avg_response = txn_total_time / txn_cnt
        avg_tps = txn_cnt / (length_millisec / 1000)
        print("{}\t{}\t{}".format(txn_name, round(avg_response, 1), round(avg_tps, 1)))


def process_results(f):
    """
    Process the JMeter CSV result file, use a dictionary store per transaction level related data,
    and it also calculate & return the test execution time as well.
    """
    start_time = 0
    end_time = 0
    txn_dict = defaultdict(list)

    try:
        with open(f, 'r', newline='') as csv_file:
            data = csv.DictReader(csv_file)

            for row in data:
                label = row['label']
                elapsed = int(row['elapsed'])

                # if it's 2nd row then get the test start time
                if data.line_num == 2:
                    start_time = int(row['timeStamp'])

                # if transaction name already exists, then populate its list by incrementing the transaction count as
                # first 1st element of list, and summing up the accumulated elapse times per transaction
                if label in txn_dict:
                    txn_dict[label][0] = txn_dict[label][0] + 1
                    txn_dict[label][1] = txn_dict[label][1] + elapsed
                # if transaction name not exit, then add transaction name as key to the dictionary for first time,
                # and then update it's value as a list [1 (transaction count), elapsed (response time)]
                else:
                    txn_dict[label].insert(0, 1)
                    txn_dict[label].insert(1, elapsed)
                # the test end time when the last row is reached otherwise it keeps getting time value
                end_time = int(row['timeStamp'])

        # calc the length of test execution time in milli seconds unit
        exec_length_millisec = end_time - start_time
        return txn_dict, exec_length_millisec
    except Exception as e:
        sys.exit('Error in parsing the csv file: {}'.format(str(e)))


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python %s <results-scrubbed-5VU.csv>" % sys.argv[0])
        sys.exit(1)

    txn_dict, exec_length = process_results(sys.argv[1])
    print_results(txn_dict, exec_length)
