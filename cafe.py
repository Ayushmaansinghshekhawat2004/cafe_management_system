#creating a dictionary for the menu
menu = {
    'Pizza':70,
    'Pasta':80,
    'Burger':50,
    'Salad':40,
    'Coffee':20
}
print("Welcome to MAAN Restaurant")
print("Pizza:70\nPasta:80\nBurger:50\nSalad:40\nCoffee:20")
order_total = 0
item_1 = input("Enter the item you want to order")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} has been added to your order")
else:
    print(f"Ordered item {item_1} isn't available in the menu yet") 
another_order = input("Do u want to order anything else (YES/NO)")
if another_order == "YES":
    item_2 = input("Enter the second item you want to order")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Your item {item_2} has been added to your order")
    else:
        print(f"Ordered item {item_2} isn't available in the menu yet")

print(f"The total amount for items you have to pay is {order_total} ") 


