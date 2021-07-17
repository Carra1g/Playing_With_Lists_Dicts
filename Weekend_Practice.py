people = [
    {"first_name" : "jo",
    "last_name"   : "momma",
    "age"         : 27,
    "city"        : "LA"},
    
    {"first_name" : "john",
    "last_name"   : "doe",
    "age"         : 25,
    "city"        : "manchester"},

    {"first_name" : "joe",
    "last_name"   : "dirt",
    "age"         : 27,
    "city"        : "grand canyon"}]

pets =  []

first_pet = {"name"    : "Max",
             "animal"  : "dog",
             "breed"   : "chiwawa",
             "owner"   : "jane"}
pets.append(first_pet) # appending pets
        
second_pet ={"name"    : "Leo",
             "animal"  : "cat",
             "breed"   : "short hair",
             "owner"   : "morticia"}
pets.append(second_pet) # appending pets
    
third_pet = {"name"    : "Poppy",
             "animal"  : "dog",
             "breed"   : "terrier",
             "owner"   : "leon"}
pets.append(third_pet) # appending pets

#list within dictionary.
favourite_places = {"New York" : ["In America", "The Big Apple", "Empire State Building"],
                    "Dublin"   : ["In Ireland", "Capial City", "The Spire"],
                    "London"   : ["In England", "House of Lords", "Buckingham Palace"]}

#adding an additional location it favoutite places.
favourite_places["Dubai"] = ["In the UAE", "Oil rich", "Burj Khalifa"]
favourite_places["Los Angeles"] = ["In America", "Hollywood", "Beverly Hills"]

for info in people:
    print("\n")
    for key, value in info.items():
        print(key.title(),":", str(value).title())
        

for pet in pets:
    print("\nHere's what i know about", pet["name"].upper() + ",")
    for key, value in pet.items():
        if key == "animal":
            print("\t\t\t",key,":",value)
        if key == "breed":
            print("\t\t\t",key," :",value)
        if key == "owner":
            print("\t\t\t",key," :",value.title())

            
for name, info in favourite_places.items():
    print("\nHeres the name of the place:",name)
    print("Heres some facts:")
    for facts in info:
        print("- " ,facts)
