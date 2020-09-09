### 2020-09-08
### Author: Andrew Gottilla
### Lesson 31: Multiple list conditional statements

# Items currently in stock
in_stock = ['Pilot G2 pen (2pk)', 'Energizer AA batteries (12pk)', 'Bang Energy variety pack (16ct)']
# Shopping cart
shop_cart = ['Pilot G2 pen (2pk)', 'Expo markers (8ct)', 'Bang Energy variety pack (16ct)', 'Energizer AA batteries (12pk)']

# 'Adding' items to cart if there are any
if shop_cart:
    for item in shop_cart:
        if item in in_stock:
            print ("ADDED: " + item + " .")
        else:
            print("ERROR: " + item + " IS OUT OF STOCK .")
    print("------------------------------------------------\nYour order is complete!")
else:
    print("You must have an item in your cart to process an order!")