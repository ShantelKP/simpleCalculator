'''Create a function named calculate_discount(price, discount_percent)
 that calculates the final price after applying a discount. 
 The function should take the original price (price) and the discount percentage (discount_percent) as parameters. 
If the discount is 20% or higher, apply the discount; otherwise, return the original price.'''



def calculate_discount(price, discount_percent):
    if discount_percent >=0.2:

        discount_amount = price  *discount_percent
        final_price= price - discount_amount

    else:
        final_price=price
    
    return(final_price)

print(calculate_discount(700, 0.4))

'''Using the calculate_discount function, 
prompt the user to enter the original price of an item and the discount percentage.
 Print the final price after applying the discount, or if no discount was applied, print the original price.'''


def calculate_discount():

    price = float(input("enter the origional price"))
    discount_percent=float(input("enter the discout"))
    final_price = price * discount_percent

    if discount_percent >0:
        discount_amount = price * discount_percent
        final_price = price - discount_amount
        print(f"Discount applied! Final price is: {final_price}")
    else:
        final_price= price
        print(f"No discount applied. Final price is: {final_price}")


    return(final_price)
calculate_discount()


