total_price = 0
number_of_item = int(input("Number of items: "))

while number_of_item < 0:
    print ("Invalid number of items!")
    number_of_item = int(input("Number of items: "))

for i in range(number_of_item):
    price_of_item = float(input("Price of item: "))
    total_price = total_price + price_of_item

if total_price > 100:
    final_price = total_price - (total_price * 0.1)
else:
    final_price = total_price
print (f"Total price for {number_of_item} items is ${final_price:.2f}")