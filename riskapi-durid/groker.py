from pygrok import Grok

class groker4durid:
    define __init__(self, )


'''
pat_JOB_START = '%{LOGLEVEL:level} %{TIMESTAMP_ISO8601:timestamp} %{WORD:component} %{NUMBER:process_num:int} %{NUMBER:thread_num:int} start load EOD_20170701_NA_19'
pat_DataFabric_END = '%{LOGLEVEL:level} %{TIMESTAMP_ISO8601:timestamp} %{WORD:component} %{NUMBER:process_num:int} %{NUMBER:thread_num:int} Files loaded in %{TIME:time}'
pat_DataLakeCMLA_END = '%{LOGLEVEL:level} %{TIMESTAMP_ISO8601:timestamp} %{WORD:component} %{NUMBER:process_num:int} %{NUMBER:thread_num:int} All Files Delivered To cmla : %{TIME:time}'
pat_DataLakeRISKIT_END = '%{LOGLEVEL:level} %{TIMESTAMP_ISO8601:timestamp} %{WORD:component} %{NUMBER:process_num:int} %{NUMBER:thread_num:int} All Files Delivered To risk_it : %{TIME:time}'
pat_DataLakeEIM_END = '%{LOGLEVEL:level} %{TIMESTAMP_ISO8601:timestamp} %{WORD:component} %{NUMBER:process_num:int} %{NUMBER:thread_num:int} All Files Delivered To eim : %{TIME:time}'
pat_ETL_END = '%{LOGLEVEL:level} %{TIMESTAMP_ISO8601:timestamp} %{WORD:component} %{NUMBER:process_num:int} %{NUMBER:thread_num:int}  All files processed in %{TIME:time}'
Pat_JOB_END = '%{LOGLEVEL:level} %{TIMESTAMP_ISO8601:timestamp} %{WORD:component} %{NUMBER:process_num:int} %{NUMBER:thread_num:int} Total execution time: %{TIME:time}'

pat_list = [pat_JOB_START, pat_DataFabric_END, pat_DataLakeCMLA_END, pat_DataLakeRISKIT_END, pat_DataLakeEIM_END,
            pat_ETL_END, Pat_JOB_END]
# print pat_list
# grok = Grok(pat_DataFabric_START)
# grok2 = Grok(pat_DataFabric_END)

with open("druidlog") as f:

    while not 'EOD_20170701_NA_19' in next(f):
        pass
    for line in f:
        pat = pat_list.pop(0)
        grok = Grok(pat)
        m = grok.match(line)
        if m is not None:
            print m
        else:
            pat_list.insert(0, pat)
    # EOF is reached
    else:
        print "ERROR: No job found"
        
    '''

    '''
    lines = f.readlines()[9710:]
    for line in lines:
        pat = pat_list.pop(0)
        grok = Grok(pat)
        m = grok.match(line)
        if m is not None:
            print m
        else:
            pat_list.insert(0, pat)
    '''

    '''
    for i in range(9710):
        f.readline()

    for line in f:
        pat = pat_list.pop(0)
        grok = Grok(pat)
        m = grok.match(line)
        if m is not None:
            print m
        else:
            pat_list.insert(0, pat)
    else:
        print "ERROR: No job found"
    '''

    '''
    for line in f:
        pat = pat_list.pop(0)
        grok = Grok(pat)
        m = grok.match(line)
        if m is not None:
            print m
        else:
            pat_list.insert(0, pat)
    else:
        print "ERROR: No job found"
    '''

