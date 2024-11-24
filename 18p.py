employee = {
    "IT": {
        "sridevi": {"age": 21, "position": "Developer", "salary": 20000000},
        "Abirami": {"age": 35, "position": "Manager", "salary": 9000000}
    },
    "HR": {
        "Dhivya": {"age": 42, "position": "HR Specialist", "salary": 60000},
        "kamal": {"age": 30, "position": "Recruiter", "salary": 50000}
    }
}

def add_employee(department, name, age, position, salary):
    if department not in employee:
        employee[department] = {}
    employee[department][name] = {"age": age, "position": position, "salary": salary}
def update_salary(department, name, new_salary):
    if department in employee and name in employee[department]:
        employee[department][name]["salary"] = new_salary
    else:
        print("Employee not found.")

def highest_salary_in_department():
    highest_salaries = {}
    for department, employees in employee.items():
        highest_salary = 0
        top_employee = ""
        for name, info in employees.items():
            if info["salary"] > highest_salary:
                highest_salary = info["salary"]
                top_employee = name
        highest_salaries[department] = top_employee
    return highest_salaries

def average_salary_in_department():
    avg_salaries = {}
    for department, employees in employee.items():
        total_salary = 0
        num_employees = len(employees)
        for info in employees.values():
            total_salary += info["salary"]
        avg_salaries[department] = total_salary / num_employees if num_employees > 0 else 0
    return avg_salaries

def transfer_employee(current_department, new_department, name):
    if current_department in employee and name in employee[current_department]:
        employee_info = employee[current_department].pop(name)
        if new_department not in employee:
            employee[new_department] = {}
        employee[new_department][name] = employee_info
    else:
        print("Employee not found.")

add_employee("HR", "Dheera", 20, "Accountant", 65000)
print(f"Updated employee dictionary after adding Dheera:\n{employee}\n")

update_salary("IT", "sridevi", 750000000)
print(f"Updated employee dictionary after updating salary of sridevi:\n{employee}\n")

print("Highest salary in each department:", highest_salary_in_department())

print("Average salary in each department:", average_salary_in_department())

transfer_employee("HR", "IT", "kamal")
print(f"Updated employee dictionary after transferring kamal:\n{employee}")
