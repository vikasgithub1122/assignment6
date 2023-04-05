import json
class Employee:
    def __init__(self, name, dob, height, city, state):
        self.name=name
        self.dob=dob
        self.height=height
        self.city=city
        self.state=state
    def __repr__(self):
        return f"Name: {self.name}, DOB: {self.dob}, Height: {self.height}, City: {self.city}, State: {self.state}"
employee_Data=[
    {
        "Name":"raja",
        "DOB": "23/11/1996",
        "Height":"6ft",
        "City":"Hisar",
        "State":"haryana"
    },
    {
        "Name":"rana",
        "DOB":20/1/1995,
        "Height":"6ft 2in",
        "City":"ludiana",
        "State":"punjab"
    },
    {
        "Name": "kisu",
        "DOB": "05/15/1990",
        "Height": "6ft 2in",
        "City": "delhi",
        "State": "DELHI"
    },
    {
        "Name": "arka",
        "DOB": "01/12/2000",
        "Height": "6ft 5in",
        "City": "lucknow",
        "State": "UP"
    },
    {
        "Name": "raman",
        "DOB": "23/11/1996",
        "Height": "5ft 8in",
        "City": "mumbai",
        "State": "MAHARASTRA"
    }
]


# write employee data to employee.json file
with open("employee.json", "w") as f:
    f.write(json.dumps(employee_Data, indent=10))
# read employee data from employee.json file
with open("employee.json", "r") as f:
    employee_data=json.load(f)
# create a list of Employee objects
employee_objects=[]
for emp in employee_Data:
    emp_obj = Employee(emp["Name"], emp["DOB"], emp["Height"], emp["City"], emp["State"])
    employee_objects.append(emp_obj)
print(employee_objects)