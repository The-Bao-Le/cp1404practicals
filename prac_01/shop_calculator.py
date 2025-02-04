DISCOUNT_THRESHOLD = 100
DISCOUNT_RATE = 0.1

total_price = 0
number_of_items = int(input("Number of items: "))
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))

for i in range(number_of_items):
    item_price = float(input("Price of item: "))
    total_price += item_price

if total_price > DISCOUNT_THRESHOLD:
    total_price *= (1 - DISCOUNT_RATE)

print(f"Total price for {number_of_items} is {total_price:.2f}")