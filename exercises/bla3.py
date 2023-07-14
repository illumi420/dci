import random

# Begginer:

def number_loop():
    result = 0
    for i in range(0, 11):
        print(i)
        result += i
       
    return f"the sum of the previous loop = {result}"

print(number_loop())



counter = 1
while counter <= 20:
    print(counter)
    counter +=1
print()    
#############################################################

    
# Intermediate:
    
def numbers_lists():
    one_to_twenty = [i for i in range(1,21)]
    squares_to_ten = [i**2 for i in range(0,11)]
    reversed_list = [i for i in range(25,4,-1)]

    return f" one to twenty: {one_to_twenty}\n Squares List: {squares_to_ten}\n a list created in reverse: {reversed_list}"


print(numbers_lists())
print()
#############################################################

# Advanced:

def is_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return number

def loops():
    x, y = 2, 30
    cubes_to_15 = [i**3 for i in range(1,16)]
    primes_between_x_and_y = [prime for prime in range(x,y) if is_prime(prime)]
    
    random_list = random.sample(range(x,y), 9)
    random_list_reversed = random_list[::-1]
    random_list_sorted = sorted(random_list_reversed)
            
    return f" The Sum of Cubes from 1 to 15 = {sum(cubes_to_15)}\n Primes between {x} and {y} {primes_between_x_and_y}\n random list: {random_list}\n reversed list: {random_list_reversed}\n sorted list: {random_list_sorted}"

print(loops())
    
