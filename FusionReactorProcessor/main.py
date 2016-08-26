if __name__ == "__main__":
    # Initialize a names dictionary(hashmap) as empty to start with.
    # Each key in this dictionary will be a name and the value
    ipsHashmap = {}
    requestLogFile = open('logs/request.log')
    for line in requestLogFile:
        # fusion reactor log uses space as delimiter
        fieldsList = line.strip().split(' ')
        ''' field mapping according to log format specs http://docs.intergral.com/pages/viewpage.action?pageId=32738148
        # Field#1       - Field#2       - Field#3       - ... - Field#7        - ... - Field#10
        # Date          - Time          - Date/Time(ms) - ... - Request Status - ... - Client IP Address
        # 2016-07-25      13:59:59.688    1469469599688         EXECUTING              142.76.18.97
        '''
        reqStatusFields=fieldsList[6]
        if reqStatusFields != 'EXECUTING':
            continue
        dateField=fieldsList[0]
        timeField=fieldsList[1]
        mstimeField=fieldsList[2]
        clientIPField=fieldsList[9]

        # key: yyyy-mm-dd-hh (as fusion reactor file is logging hourly)
        # value: a set (distinct) of client IP in hourly interval
        #  and value ('2016-07-25-13', set(['142.76.154.23', '142.76.7.219', '142.76.115.99']))
        key_ipsHashmap = dateField + "-" + timeField.split(':')[0]
        value_ipsHashmap = clientIPField
        # if key is not in dictionary then starting with an empty set, which will eliminate duplicates(e.g. IPs)
        # else key is present then add IPs to a set which current key is referring to
        if key_ipsHashmap not in ipsHashmap:
            ipsSet = set()
            ipsSet.add(value_ipsHashmap)
            ipsHashmap[key_ipsHashmap] = ipsSet
        else:
            ipsHashmap[key_ipsHashmap].add(value_ipsHashmap)

    requestLogFile.close()

    for key, value in ipsHashmap.items():
        print("@time[yyyy-mm-dd-hh]: " + key + ", has a total of distinct client IPs: " + str(len(value)) + ", with IP " + str(value))