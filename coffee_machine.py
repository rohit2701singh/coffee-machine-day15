from art import logo
from menu_item import MENU, profit, resources


def report_resources_left(user_coffee_choice):
    """it will deduct resources based on user's coffee choice."""
    for item in MENU[user_coffee_choice]["ingredients"]:
        # by doing this we do not have to think about the items in particular coffee, like in espresso(milk).
        resources[item] -= MENU[user_coffee_choice]["ingredients"][item]


def checking_resources(user_coffee_choice):
    for item in MENU[user_coffee_choice]["ingredients"]:
        if resources[item] < MENU[user_coffee_choice]["ingredients"][item]:
            print(f"{item} is not sufficient in the machine to make {user_coffee_choice}.🍵🍶")
            return False
    return True


print(logo)
want_coffee = True
while want_coffee:
    print("==================================================================\n")

    user_choice = input("what would you like? (espresso/latte/cappuccino/report/off): ")
    if user_choice == "report":
        print(f"water: {resources['water']} ml\nmilk: {resources['milk']} ml\ncoffee: {resources['coffee']} gm\nmoney: "
              f"$ {profit}")
    elif user_choice == "off":
        print("coffee machine is off now.")
        want_coffee = False

    elif checking_resources(user_choice):
        # above line is: elif checking_resources(user_choice)==True
        print("please insert coins.")
        quarters = int(input("how many quarters (1Q=$0.25)? : "))
        dimes = int(input("how many dimes (1D=$0.10)? : "))
        nickles = int(input("how many nickles (1N=$0.05)? : "))
        pennies = int(input("how many pennies (1P=$0.01)? : "))


        def user_inputs_detail(coffee_choice, quarter_coin, dime_coin, nickle_coin, penny_coin):
            """this function takes coins and user's coffee choice, then it calculates total amount based on which
            it either provides coffee or refund the money if money is not sufficient."""

            total_inserted_coin = round(quarter_coin * 0.25 + dime_coin * 0.10 + nickle_coin * 0.05 + penny_coin * 0.02, 2)
            print(f"total_inserted_amount: $ {total_inserted_coin}")
            print(f"{coffee_choice} price: $ {MENU[coffee_choice]['cost']}")

            if total_inserted_coin < MENU[coffee_choice]["cost"]:
                print("Sorry, that's not enough money. Money refunded.")

            elif total_inserted_coin >= MENU[coffee_choice]["cost"]:
                refund = round(total_inserted_coin - MENU[coffee_choice]["cost"], 2)
                report_resources_left(coffee_choice)

                global profit
                profit += MENU[coffee_choice]["cost"]
                print(f"Here is your change amount: $ {refund}")
                print(f"here is your '{coffee_choice}' ☕🍵, ENJOY!")


        user_inputs_detail(user_choice, quarters, dimes, nickles, pennies)

print(f"total profit: {profit}")
