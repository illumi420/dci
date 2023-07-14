string_reverser = lambda string = input("Please enter a String to reverse: "): string[::-1]
print("reversed:",string_reverser())

return_largest = lambda x = int(input("Please Enter First Number: ")), y = int(input("Please Enter Second Number: ")): x if x > y else y 
print("Largest =",return_largest())

sum_input_list = lambda how_many = int(input("Enter how many numbers to Input in List: ")): sum([int(input("Enter a Number: ")) for i in range(how_many)])
print("Inputed Numbers sum Equals to",sum_input_list())
