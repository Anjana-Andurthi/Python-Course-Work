'''
import json

with open("data.json",'r') as file:
    data=json.load(file)

data["Username"]="Amani"   
data["Skills"].append("Flask") 

with open("data.json",'w') as file:
    json.dump(data,file,indent=4)
'''
import json
student={
    "name":"Anjana",
    "age":21,
    "course":"Python"
}
json_data=json.dumps(student)
print(json_data)
print(type(student))

student=json.loads(json_data)
print(student)
print(type(student))