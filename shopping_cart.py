

shopping_cart = {}

def show_cart():
    if not shopping_cart:
        print("\nYour cart is empty.\n")
        return
    print("\n--- Your Shopping Cart ---")
    total = 0
    for item, details in shopping_cart.items():
        price = details['price']
        quantity = details['quantity']
        subtotal = price * quantity
        print(f"{item.title()} - R{price:.2f} x {quantity} = R{subtotal:.2f}")
        total += subtotal
    print(f"\nTotal cost: R{total:.2f}\n")

def save_cart():
    with open("shopping_cart.txt", "w") as file:
        file.write("--- Shopping Cart Summary ---\n")
        total = 0
        for item, details in shopping_cart.items():
            price = details['price']
            quantity = details['quantity']
            subtotal = price * quantity
            file.write(f"{item.title()} - R{price:.2f} x {quantity} = R{subtotal:.2f}\n")
            total += subtotal
        file.write(f"\nTotal cost: R{total:.2f}\n")
    print("Cart saved to 'shopping_cart.txt'\n")

print("🛒 Welcome to Lucky Kali SuperMarket!")
print("Enter 'done' to finish, 'remove' to delete an item, or 'view' to see your cart.\n")

while True:
    action = input("Enter food item or command (done/remove/view): ").strip().lower()
    
    if action == 'done':
        break
    elif action == 'view':
        show_cart()
        continue
    elif action == 'remove':
        item_to_remove = input("Enter the item to remove: ").strip().lower()
        if item_to_remove in shopping_cart:
            del shopping_cart[item_to_remove]
            print(f"{item_to_remove.title()} removed from cart.\n")
        else:
            print(f"{item_to_remove.title()} not found in cart.\n")
        continue
    
    item = action
    try:
        price = float(input(f"Enter the price of '{item}': R"))
        quantity = int(input(f"Enter quantity of '{item}': "))
    except ValueError:
        print("⚠️ Invalid input. Please enter numeric values for price and quantity.\n")
        continue

    if item in shopping_cart:
        shopping_cart[item]['quantity'] += quantity
    else:
        shopping_cart[item] = {'price': price, 'quantity': quantity}
    
    print(f"✅ {item.title()} x {quantity} added to cart.\n")


show_cart()


save = input("Do you want to save your cart to a file? (yes/no): ").strip().lower()
if save == 'yes':
    save_cart()

print("🛍️ Thank you for shopping with us, Siyabonga!")
