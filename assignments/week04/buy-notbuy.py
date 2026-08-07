def main():
    prices = []
    for i in range(6):
        price = float(input(f"Enter price for item {i + 1}: "))
        prices.append(price)

    budget = float(input("Enter total budget: "))
 
    total_spent = 0
    bought_items = []
 
    print("\n--- Checking items in order ---")
 
    for index, price in enumerate(prices):
        
        if total_spent + price <= budget:
            total_spent += price
            bought_items.append(price)
            print(f"Item {index + 1} (price {price:.2f}) -> buy")
        else:
            print(f"Item {index + 1} (price {price:.2f}) -> cannot buy")
 
    remaining_budget = budget - total_spent
    print("\n--- Summary ---")
    print(f"Items bought: {bought_items}")
    print(f"Total spent: {total_spent:.2f}")
    print(f"Remaining budget: {remaining_budget:.2f}")
 
 
if __name__ == "__main__":
    main()