def sum_number_pairs(input_file, output_filename):
    """ (file open for reading, str) -> NoneType
    Read the data from input_file, which contains two floats per line
    separated by a space.  Open file named output_file and, for each line in
    input_file, write a line to the output file that contains the two floats
    from the corresponding line of input_file plus a space and the sum of the
    two floats.
    """
    with open(output_filename, 'w') as output_file:
        output_file.write("this is kang's first write-out test\n")


sum_number_pairs("number_pairs.txt","number_out.txt")