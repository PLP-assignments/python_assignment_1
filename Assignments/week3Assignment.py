def calculate_discount(price,discount_percent):
    if discount_percent >=20:
        return price * (1-discount_percent/100)
    else:
        return price

#prompting the user to enter the original price and discount percentage of the item
original_price = float(input("Enter the original price price of the item: "))
discount_percentage = float(input("Enter the discount percentage value: "))

#calculating the final price after applying the discount percentage
final_price = calculate_discount(original_price,discount_percentage)

if final_price == original_price:
    print("No discount applied. The Final price is:", final_price)
else:
    print("Final price after applying the discount:", final_price)