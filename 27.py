import csv
with open(r"C:\Users\dhivy\OneDrive\Documents\employee_salary.csv","r")as file:
        reader=csv.reader(file)
        print("employee salary details")
        for row in reader:
            print(row)
       

extracted_data=[]
for data in extracted_data:
      emp_id=row[emp_id]
      doj=row[doj]
      netpay=row[netpay]
extracted_data.append([emp_id,doj,netpay])
print(data) 