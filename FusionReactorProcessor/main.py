if __name__ == "__main__":
    # Initialize a names dictionary as empty to start with.
    # Each key in this dictionary will be a name and the value
    names = {}
    observations_file = open('request.log')
    for line in observations_file:
            strline = line.strip()
            k,v = strline.split(' ')
            if k not in names:
                s = set()
                s.add(v)
                names[k] = s
            else:
                names[k].add(v)

    observations_file.close()

    for key, value in names.items():
        print(key, value)