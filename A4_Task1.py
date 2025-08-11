try:
    # Method 1
    '''
        file = open("sample.txt", "r")
        print("Reading file content:")
        reading_file = file.read()
        print(reading_file)
        file.close()
    '''

    # Method 2
    with open("sample.txt", "r") as file:
        print("Reading file content:")
        reading_file = file.read()
        print(reading_file)
        # for line in file:            
        #     print(line.rstrip())

except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")