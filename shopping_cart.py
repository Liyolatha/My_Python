#Shopping cart programme that will continuasiouly ask the user to enter food products and the price of that product.
#Have an exit claus if the user wishes to stop adding more things to the cart.
#At the end show all the food items and the cost to the user.

foods = []
prices = []
total = 0

while True:
    food = input("Enter the food you want to buy or enter q to quit ")
    if food == "q":
        break 
    else:
        price = float(input(f"Enter the price of the {food}: R"))
        foods.append(food)
        prices.append(price)
        
print("---YOUR CART---")

for food in foods:
    print(food, end= " ") #Use end to show the cart horizontal
    
for price in prices:
    total += price
 
print("\n") 
print(f"Your total is: R{total}")