from csv_projects_funcs import csvToDictsList
import random

        

dict_list = csvToDictsList("movie_data.csv")



print("Movies: ")
print()

movies = []
genere_list = []
ratings = []
years = []

for movie in dict_list:
    for key, value in movie.items():
        print(key, value)
        movies.append(key)
        genere_list.append(movie[key]['genre'])
        ratings.append(movie[key]['rating'])
        years.append(movie[key]['year'])
print()
#print(genere_list)
#print(ratings)

genere_uniq = set(genere_list)
#print(genere_uniq)

genere_count = {}
genere_avereage = {}
years_count = {}

for genere in genere_uniq:
    genere_count[genere] = genere_list.count(genere)
    genere_avereage[genere] = sum([float(ratings[i])/genere_count[genere] for i,g in zip(range(len(ratings)), genere_list) if g == genere])
    
for year in years:
    years_count[year] = years.count(year)

print(f" Total Generes: {genere_count}\n Generes Average Ratings: {genere_avereage}\n Movies count by Year: {sorted(list(years_count.items()))}")    

print()

random_movie = random.choice(movies)

for i in dict_list:
    for key,value in i.items():
        if key == random_movie:
            print(f" Recommended Movie: {random_movie} {value}")


