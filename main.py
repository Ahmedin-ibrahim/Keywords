# Snack Vending machine

# PART 1: A function that works out change and sends it back with return
def calculate_change(paid, price):
    change = paid - price
    return change

# PART 2: Set the snack price and greet the customer
snack_price = 25
print("===== SNACK VENDING MACHINE =====")
print("This snack costs", snack_price, "units.")
print("Accepted coins: 1, 5, 10, 25\n")

total_inserted = 0
coins_inserted = 0

# PART 3: Keep accepting coins until enough money has been inserted
while True:
    coin = int(input("Insert a coin (1, 5, 10, 25): "))

    #part 4: Check if the coin is valid
    if coin != 1 and coin != 5 and coin != 10 and coin != 25:
        print("Invalid coin. Please insert a valid coin.")
        continue

    #part 5: Add the valid coin to the running total 
    total_inserted += coin
    coins_inserted += 1
    print(f"Inserted: {coin}. Total so far: {total_inserted} \n")

    #part 6: Stop accepting coins if enough money has been inserted
    if total_inserted >= snack_price:
        print("Enough money has been inserted.")
        break

#part 7: Work out the change using the value returned by calculate_change
change_due = calculate_change(total_inserted, snack_price)

print("Dispensing your snack . . .")

#part 8: Nothing extra to do when the change is exactly zero
if change_due > 0:
    pass
else:
    print("Here is your change:", change_due, "units.")

#Part 9: Print a short summury of the purchase
print("\n===== PURCHASE SUMMARY =====")
print("Snack price:", snack_price, )
print("Coins inserted:", coins_inserted)
print("Total paid:", total_inserted)
print("Change given:", change_due)
print("================================")
print("Thank you for your purchase!")
# End of program