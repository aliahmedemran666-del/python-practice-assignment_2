c_name = input("")

li = []


for i in range(1, 4):
    p_name = input(f"product {i} name: ")
    price = int(input(f"product {i} price: "))
    li.append({"name": p_name, "price": price})

total = 0

for i in li:
    total += i["price"]


if total>=5000:
    discount_rate = 0.20
elif total>=3000 and total<=4999:
    discount_rate = 0.10
elif total>=1000 and total<=2999:
    discount_rate = 0.05
elif total<1000:
    discount_rate = 0

discount = total * discount_rate
final_total = total - discount

print(f"\nCustomer Name: {c_name}")

for i in range(3):
    product = li[i]
    n = i + 1
    print(f"Product {n}: {product['name']}")
    print(f"Price: {product['price']}")

print(f"Subtotal: {total}")
print(f"Discount: {discount}")
print(f"Final Total: {final_total}")