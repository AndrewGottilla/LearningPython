### 2020-09-08
### Author: Andrew Gottilla
### Lesson 30: List conditional statements

# Shopping cart
shop_cart = ['Pilot G2 pen (2pk)', 'Expo markers (8ct)', 'Bang Energy variety pack (16ct)', 'Energizer AA batteries (12pk)']

# 'Adding' items to cart if there are any
if shop_cart:
    for item in shop_cart:
        if item == "Bang Energy variety pack (16ct)":
            print("Sorry! " + item + " is currently out of stock.")
        else:
            print ("Adding " + item + " to your order.")
    print("------------------------------------------------\nYour order is complete!")
else:
    print("You must have an item in your cart to process an order!")
