def list_categorizer(a_list):

    num_list = [i for i in a_list if type(i) == int or type(i) == float]
    string_list = [w for w in a_list if type(w) == str]

    int_list = []
    float_list = []
        
    for n in num_list:
        if type(n) == int:
            int_list.append(n)
        else:    
            float_list.append(n)
        
    return f" Mixed List: {a_list}\n Numbers List: {num_list}\n Strings List: {string_list}\n Integers List: {int_list}\n Floats List: {float_list}"


mixed_list = ["what", 9, "how", 6.3, "why", 420]

print(list_categorizer(mixed_list))
