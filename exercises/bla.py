def greatest_num(*numbers):
    return max(numbers)


print(greatest_num(1,2,3))

################################################################################

def day_input():
    days = {
            1:"Sunday",
            2:"Monday",
            3:"Tuesday",
            4:"Wedensday",
            5:"Thursday",
            6:"Friday",
            7:"Saturday"
        }

    user_input = int(input("Please Enter a Number between 1 and 7 to Output a day: "))
    return days[user_input]


print(day_input())
print()


################################################################################


def number_input():
    first_num = float(input("Please Enter First Number: "))
    second_num = float(input("Please Enter Second Number: "))

    if first_num > second_num:
        return f"{first_num} is greater than {second_num}"

    elif second_num > first_num:
        return f"{second_num} is greater than {first_num}"

    else:
        return f"{first_num} is equal to {second_num}"

print(number_input())        
print()
