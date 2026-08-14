product_name=str(input("enter product name:"))
product_quantity=int(input("enter product quantity:"))
product_price=float(input("enter product price:"))
product=(product_name,product_quantity,product_price)
print(product)
calculated_price=product_quantity*product_price
print("calculated price is:",calculated_price)