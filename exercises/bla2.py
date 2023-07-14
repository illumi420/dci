def do_numbers():
    user_input = int(input(" Please Enter a Number: "))

    zero_positive_negative = lambda user_input: f"{user_input} is Positive number" if user_input > 0 else f"{user_input} is Negative number" if user_input < 0  else f"{user_input} equal to zero"


    def is_leap(user_input):
        year_divisible_by_4 = user_input % 4 == 0
        year_divisible_by_100 = user_input % 100 == 0
        year_divisible_by_400 = user_input % 400 == 0

        

        if (year_divisible_by_4 and year_divisible_by_100 and year_divisible_by_400) or (year_divisible_by_4 and not year_divisible_by_100):
            return f"{user_input} is a leap year"
        return f"{user_input} is not a leap year"

     

    even_odd = lambda user_input: f"{user_input} is even number" if  user_input % 2 == 0 else f"{user_input} is odd number"  

    def is_prime(number):
        if number > 1:
            for i in range(2, number):
                if number % i == 0:
                    return f"{number} is not a prime number"
            return f"{number} is a prime number"
        else:
            return f"{number} is not positive"

    return zero_positive_negative(user_input), is_leap(user_input), even_odd(user_input), is_prime(user_input)    


print(do_numbers())


def do_strings():
    print()
    string = input("Please Enter a word: ")
    if string == string[::-1] :
        return f"{string} is  palindrome"
    return f"{string} is not palindrome"

print(do_strings())
