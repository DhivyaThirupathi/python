products = {}
while True:
    product_name = input("Enter the product name to add (or type 'done' to stop adding): ")
    if product_name.lower() == 'done':
        break
    product_price = float(input("Enter the product price: "))
    products[product_name] = product_price
    print(f"Product {product_name} added with price {product_price}")

while True:
    query = input(
        "Enter 'price' to check a product price, 'less' to list products under a price, or 'quit' to exit: ").lower()
    if query == 'quit':
        break

    if query == 'price':
        product_name = input("Enter a product name to check its price: ")
        if product_name in products:
            print(f"The price of {product_name} is {products[product_name]}")
        else:
            print(f"{product_name} is not in the dictionary.")

    elif query == 'less':
        price_threshold = float(input("Enter the amount: "))
        cheaper_products = [name for name, price in products.items() if price < price_threshold]
        if cheaper_products:
            print("Products priced under", price_threshold, "are:", cheaper_products)
        else:
            print(f"No products priced under {price_threshold}.")
    else:
        print("Invalid input.")

print("\nFinal list of products and prices:")
for name, price in products.items():
    print(f"{name}: {price}")
