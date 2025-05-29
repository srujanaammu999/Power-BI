''' Create a class with department which has dept ID, dept name,location and head of dept through the constructor initialize the department attributes create a method to display the dept information
display total depatments in your organization'''

'''Get the input from the user as no.of depts and create a list or dictionary
use for loop to get dept information and store it in the list or dictionary'''

'''Search dept by dept id - user will enter dept id show details of that dept if present
if not present show message that dept not found
add a function to search dept by name - user will enter dept name show details of that dept if present'''


class Department:
    def __init__(self, dId, dname, location, head):
        self.dId = dId
        self.dname = dname          
        self.location = location
        self.head = head
    def display_dept_info(self):
        print(f"Department information:")
        print("-----------------------")
        print(f"Department Id: {self.dId}")
        print(f"Department Name: {self.dname}")
        print(f"Location: {self.location}")
        print(f"Head: {self.head}")

dept_count = int(input("Enter no. of departments: "))
# Dictionary to store department objects using ID as key
depts = {}
# Input department details from users
for i in range(dept_count):
    dId = input(f"Enter Department Id for department {i+1}: ")
    dname = input(f"Enter Department Name for department {i+1}: ")
    location = input(f"Enter Location for department {i+1}: ")
    head = input(f"Enter Head for department {i+1}: ")
    department = Department(dId, dname, location, head)
    depts[dId] = department
# Displaying all department information
for dept in depts.values():
    dept.display_dept_info()

# Function to search department by ID and name
def searchBy_id():
    dept_id = input("\nEnter Department ID to search: ")
    dept = depts.get(dept_id)
    if dept:
        dept.display_dept_info()
    else:
        print("Department with the given ID is not available.")
# Function to search department by name
def searchBy_name():
    dept_name = input("\nEnter Department Name to search: ")
    found = False
    for dept in depts.values():
        if dept.dname.lower() == dept_name.lower():
            dept.display_dept_info()
            found = True
    if not found:
        print("Department with the given name is not available.")

# Calling functions
searchBy_id()
searchBy_name()
