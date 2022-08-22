programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}

programming_dictionary["Loop"] = "The action of doing something over and over again."

print(programming_dictionary["Bug"])

#Create an empty dictionary
empty_dictionary = {}
    #programming_dictionary = {}

#Edit and item in dictionary
programming_dictionary["Bug"] = "A moth in your computer"

print(programming_dictionary)

# Loop through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])


###############################################
#Nesting
travel_log = {
    "France" : {"cities_visited" : ["Paris", "Lille", "Dijon"], "total_visits" : 12},
    "Germany" : {"cities_visited" : ["Berlin", "Hamburg", "Stuttgrat"], "total_visits" : 5}
}

#Nesting Dictionaries in a list
travel_log = [
    {
        "counntry" : "France", 
        "cities_visited" : ["Paris", "Lille", "Dijon"], 
        "total_visits" : 12
    },
    {
        "country" : "Germany", 
        "cities_visited" : ["Berlin", "Hamburg", "Stuttgrat"], 
        "total_visits" : 5
    }
]
