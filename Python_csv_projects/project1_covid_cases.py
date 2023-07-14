from csv_projects_funcs import csvToDictsList
import random


dict_template = csvToDictsList('covid.csv')
list_keys = []
sum_cases = 0
sum_deaths = 0
sum_recovered = 0

print("Covid Cases:")
print()

for case in dict_template:
    for key, value in case.items():
        print(key,value)
        list_keys.append(key)
        sum_cases += int(case[key]["new_cases"])
        sum_deaths += int(case[key]["deaths"])
        sum_recovered += int(case[key]["recovered"])
print()


print(f" Total Cases: {sum_cases}\n Total Deaths: {sum_deaths}\n Total Recovered: {sum_recovered}")
print()

print(f" Cases Average: {sum_cases/len(list_keys)}")
print()

random_day = random.choice(dict_template)
print(f" in This Day {random_day}")
       
