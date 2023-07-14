import re

def insulin(new_file,char_range_from,char_range_to):
    

    temp_string = " "

    pattern = re.compile('[a-z]')

    file = open("preproinsulin-seq.txt", "r")

    for line in file:
        if re.search(pattern, line):
            temp_string += line
    file.close()     

    #print(temp_string)

    for char in temp_string:
        if char.isnumeric() or char == "\n" or char == " ":
            temp_string = temp_string.replace(char, "")

    #print(temp_string)        

    file1 = open("preproinsulin-seq-clean.txt", "w")
    file1.write(temp_string)
    file1.close()

    file2 = open(new_file, "w")
    file2.write(temp_string[char_range_from:char_range_to])
    file2.close()


insulin("lsinsulin-seq-clean.txt",1,24)
insulin("binsulin-seq-clean.txt",25,54)
insulin("cinsulin-seq-clean.txt",55,89)
insulin("ainsulin-seq-clean.txt",90,110)

