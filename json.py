#Import the json python library
import json


#Create the data dictionary

data = {

    'name': 'Jose Rocha',
    'age':27,
    'city':'Seattle,WA',
    'interests': ['gym','basketball','videogames'],
    'is_student': True
    
}

# This opens the file as json_file
with open('data.json','w') as json_file:

    json.dump(data,json_file,indent=4)

print('Data has been written to data.json')

#
with open('data.json','r') as json_file:

    loaded_data = json.load(json_file)

print("Successfully able to read data.json")
print(loaded_data)
