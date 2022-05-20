travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇

country = input("Name a country: ")
visits = input("How many visits: ")
cities = input("Name a city: ")


def add_new_country(country, visits, cities): #parameter
    new_country = {"country": country, "visits": visits, "cities": cities} #inside the function you create a new dictionary then append it to the original
    travel_log.append(new_country)


#🚨 Do not change the code below
add_new_country(country, visits, cities) #argument, argument is not a dictionary, thats why I have to create one, line 19.
print(travel_log)

########################################################################

cities = ["London", "New York"]
for city in cities:
    print(city) ## Prints every city

gender = {"Adrian": Male, "Mateo": Male}
for sex in gender:
    print(sex, gender[sex]) ## Prints every name and gender.