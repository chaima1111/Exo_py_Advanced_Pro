cities ={}
while True:
    city = input("enter a city name: ").lower()
    if city == "stop":
        break
    else:
        population = len(city) *1000000
        cities.update({city : population})
        
cities = dict(sorted(cities.items(), key=lambda item: item[1], reverse=True))

print("---------------------CITIES---------")
for city , pop in cities.items():
    print(f"{city} : {pop}")
