print("Hello, Python!\n")
while True:
    
    def menu():
        print()
        print("Please choose from the following:")
        print("  1. Simple Arethmetics calculations on two numbers\n",
              " 2. Square of a Number\n",
              " 3. Concatenate two Strings\n",
              " 4. Uppercase a STRING\n",
              " q. quit",)
        user_input = input(" Option Value: ")

        if user_input == "1":
            num1 = float(input("Please Enter first Number: "))
            num2 = float(input("Please Enter second Number: "))
            exercise(num1,num2)
            print()

        elif user_input == "2":
            num = float(input("Please Enter a Number: "))
            exercise(num)
            print()

        elif user_input == "3":
            word1 = input("Please Enter first string: ")
            word2 = input("Please Enter second string: ")
            exercise(word1,word2)

        elif user_input == "4":
            word = input("Please Enter a string: ")
            exercise(word)

        else:
            quit()
            
        
    def exercise(*params):
        if len(params) == 2 and ( isinstance(params[0], float) == True ):
            try:
                print()
                print(f"The sum of {params[0]} + {params[1]} =",params[0]+params[1])
                print(f"The substraction of {params[1]} - {params[0]} =",params[1]-params[0])
                print(f"The multiplication of {params[0]} * {params[1]} =",params[0]*params[1])
                print(f"The division of {params[1]} / {params[0]} =",params[1]/params[0])
                print(f"The reminder from dividing {params[1]} / {params[0]} =",params[1]%params[0])
            except:
                print("something wrong")

        elif ( len(params) == 1 ) and ( isinstance(params[0], float) == True ):
            print()
            print(f"The Square of {params[0]} =",params[0]**2)


        elif ( len(params) == 2 ) and ( isinstance(params[0], str) == True ):
            print()
            print(f"Concatenated Strings ",params[0]+params[1] )

        elif ( len(params) == 1 ) and ( isinstance(params[0], str) == True ):
            print()
            print(f"Uppercase String:",params[0].upper())


    menu()     




