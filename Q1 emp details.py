import json
employee={    
    "employee_details":[
       {
            "emp_name" : "Sriharsha",
            "DOB" : "18/12/2000",
            "Height" : "5.2",
            "City" : "Hyderabad",
            "State" : "Telangana"
        },
         {
            "emp_name" : "Veena",
            "DOB" : "26/02/2000",
            "Height" : "5.3",
            "City" : "Warangal",
            "State" : "Telangana"
        },
         {
            "emp_name" : "Sadhana",
            "DOB" : "20/02/2001",
            "Height" : "5.3",
            "City" : "Vizag",
            "State" : "Andhra Pradesh"
        },
         {    
            "emp_name" : "Deepu",
            "DOB" : "26/12/2000",
            "Height" : "5.2",
            "City" : "Chennai",
            "State" : "Tamilnadu"
        },
         {
            "emp_name" : "Ammu",
            "DOB" : "22/06/2000",
            "Height" : "5.2",
            "City" : "Bangalore",
            "State" : "Karnataka"
        }
    ]
}          
with open("employee.json","w") as outfile:
    json.dump(employee,outfile,indent=2)

f = open('employee.json', "r")
data = json.loads(f.read())
for i in data["employee_details"]:
    print(i)
f.close()    


#Create a dictionary of any 7 Indian states and their capitals. Write this into a JSON file.

import json

Indian_States = {
        "Telangana":"Hyderabad",
        "Andhra Pradesh":"Amaravathi",
        "Tamilnadu":"Chennai",
        "Rajasthan":"Jaipur",
        "Delhi":"New Delhi",
        "Maharastra":"Mumbai",
        "Karnataka":"Bangalore"}

with open("Indian_States.json","w") as outfile:
    json.dump(Indian_States,outfile, indent=1)
print("JSON got Appended :\n",Indian_States)