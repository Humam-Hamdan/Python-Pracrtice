dict1 = {'alice': '2341', 'beth': '9102', 'cecil': '3258'}

print(dict1)

dict2 = {'name': 'zara', 'age': 7, 'class': 'first'}

print(dict2)

print(dict1['alice'], dict2['name'])

dict2['name'] = 'humam'

print(dict2)

dict3 = {'name': 'zara', 'age': 7, 'class': 'first'}

dict3['age'] = 8

dict3['school'] = 'DPS school'

print(dict3)

"""
# deleting

del "dict name"[key] # remove key and entry

"dict name".clear # deletes all keys and entries

del "dict name" # delete dictionary all along
"""
dict4 = {'name': 'zara', 'age': 7, 'class': 'first', 'name': 'huda'}

print(dict4)

# dict takes the last key entry if they're more than one with the same key

"""
# Methods

"dict name".copy # copy the dict

"dict name".fromkeys() # searches for values for the keys in the last dict and insert'em all to new dict

"dict name".get(key) # returns with the value of the key

"dict name".items() # displays a list of the keys with the values

"dict name".keys() # returns with list of the keys in the dictionary

"dict name".setdefault # set a default value to the key used

"dict name".update # adds the key and values from one dict to another

"dict name".values # list of the values
"""