# this is dictionary

studen1 = {"name": "Md. Shifat",
           "age": 21,
           "gender": "M",
           "mobile": "8801733662434",
           "marks": [89, 59, 86, 95, 68, 95, 78, 59]
           }

print(list(studen1.keys()))  # print the keys of the dictionary
print(studen1.values())  # print the values of the dictionary

studen1.update({"location": "Cumilla", "age": 20})  # update the dictionary

# print(studen1.items())  # print the key,values of the dictionary


# use get method so that you cannt face any errors
print(studen1.get("location"))  # print the location of the dictionary
print(studen1["location"])  # print the location of the dictionary
