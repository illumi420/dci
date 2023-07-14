from countryinfo import CountryInfo
import random


for i in ["Apple", "Banana", "Strawberry", "Cherry"]:
    print(i)


print()
#country = input("Please Enter Counrty, to get it's Capital City: ")
#print(CountryInfo(country).capital())


positive_negative = lambda ran_num = random.randrange(-999,999): f"{ran_num} is Positive" if ran_num > 0  else f"{ran_num} is Negative" if ran_num > 0 else f"{ran_num} is zero" 

print(positive_negative())


