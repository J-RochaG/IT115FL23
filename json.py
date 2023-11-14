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

#This allows you to open the file succesfully and able to read.
with open('data.json','r') as json_file:

    loaded_data = json.load(json_file)

print("Successfully able to read data.json")
print(loaded_data)

#Modify the Json data. we add a string to append.
loaded_data['age'] = 27
loaded_data['interests'].append('sports')

#We modify the JSon file. 
with open('data.json', 'w') as json_file:
    
    json.dump(loaded_data, json_file, indent=4)

print('Modified data written to data.json')