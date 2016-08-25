if __name__ == "__main__":
    # Initialize a names dictionary as empty to start with.
    # Each key in this dictionary will be a name and the value
    # will be the number of times that name appears.
    names = {}
    observations_file = open('request.log')
    for line in observations_file:
            #print(line)
            strline = line.strip()
            k,v = strline.split(' ')
            if k not in names:
                names[k] = v

    observations_file.close()

    for key, value in names.items():
        print(key, value)