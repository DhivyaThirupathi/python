Q1=”I-1”
Q2=”I-2”
Q3=”I-3”
sales_data = [ [(Q1, 150), (Q2, 110), (Q3, 120)],
 [(Q1, 70), (Q2, 80), (Q3, 100)],
 [(Q1, 120), (Q2, 150), (Q3, 180)]]

sum=0
empty=[]
#problem a Computes the total sales for each product
total=[]
sum=0
for I in sales_data:
    for tup,value in i:
        sum=sum+value
    total.append(sum)
    sum=0
c=1
for I in total:
    print(f”Total Sales of each product {c}:”,i)
    c=c+1

# problem b Identifies the product with the highest average sales per quarter.

emp=[]
for I in total:
    emp.append(round(i/3))
max_m=max(emp)
for I in range(len(emp)):
    if(max_m==emp[i]):
        print(f”The product with the highest average sales per quarter is Product:”,i+1)
# problem c Sorts the products based on total sales in descending order and displays the result.
print(“The products based on total sales in descending order :”)
t=len(total)
print(“Total Sales “)
for I in range(len(total)):
    print(“Product”,t,total[i-1])
    t=t-1
# problem d Normalizes the sales for each product
normalized_sales_data = []
for product in sales_data:
    sales_values = [sale[1] for sale in product]
    min_sales = min(sales_values)
    max_sales = max(sales_values)

    normalized_sales = [(sale[0], (sale[1] – min_sales) / (max_sales – min_sales)) for sale in product]
    normalized_sales_data.append(normalized_sales)

print(“Normalized sales for each product:”)
for I, normalized in enumerate(normalized_sales_data):
    print(f”Product {I + 1}:{normalized}”)
