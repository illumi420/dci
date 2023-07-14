import csv

def csvToDictsList(csv_file):
    """
    This function returns a list of keys (from csv file first attribute values)
    these keys in the list have a dict as value, the value dict contains the
    rest of the csv file attributes as keys assigned to their respective values
    """

    dict_list = []
    attributes = []
    temp_attributes = []

    with open(csv_file) as csvFile:
        csvReader = csv.reader(csvFile, delimiter=',')
        lineCount = 0
        for row in csvReader:
            if lineCount == 0:
                # get attributes (first line in csv file values) in attributes list
                attributes.append(row)
                lineCount += 1

            else:
                # get all attributes in csv head, but the first one
                temp_attributes = attributes[0][1:]
                # create a list of keys as movie name
                # dynamicly adding dict to lists keys as value by itterating over the rest of
                # attributes.
                dict_list.append({
                    row[0] : {attr : row[temp_attributes.index(attr)+1] for attr in temp_attributes}
                    })
                lineCount +=1
                
    return dict_list     
#print(csvToDictsList("movie_data.csv"))
