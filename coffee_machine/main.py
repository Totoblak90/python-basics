import tkinter as tk
from tkinter import simpledialog


class CoinInserter(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Insert Coins")
        self.geometry("200x200")

        self.coin_types = [
            "Quarters (0.25)", "Dimes (0.10)", "Nickels (0.05)", "Pennies (0.01)"]
        self.coin_values = {"Quarters (0.25)": 0.25, "Dimes (0.10)": 0.10,
                            "Nickels (0.05)": 0.05, "Pennies (0.01)": 0.01}
        self.coin_count = {coin: 0 for coin in self.coin_types}

        self.listbox = tk.Listbox(self)
        self.listbox.pack(fill=tk.BOTH, expand=1)
        for coin in self.coin_types:
            self.listbox.insert(tk.END, coin)

        self.listbox.bind("<Return>", self.on_return)

    def on_return(self, event):
        selected_coin_type = self.listbox.get(self.listbox.curselection())
        coin_number = simpledialog.askinteger(
            "Input", f"How many {selected_coin_type}?", parent=self)
        if coin_number is not None:
            self.coin_count[selected_coin_type] += coin_number
            print(f"Inserted {coin_number} {selected_coin_type}.")

    def get_total_money(self):
        total_money = sum(
            self.coin_count[coin_type] * self.coin_values[coin_type] for coin_type in self.coin_types)
        return total_money


total_resources = {
    "water": 1000,
    "milk": 500,
    "chocolate": 500,
    "sugar": 500,
    "coffee": 2000,
    "profit": 0.0
}


def select_coffee_type():
    return input("What would you like? (espresso/latte/cappuccino): ")


def check_resources(selected_coffee_type: str):
    for key in selected_coffee_type:
        if key in total_resources and selected_coffee_type[key] > total_resources[key]:
            return key

    return False


def update_resources(selected_coffee_type: dict):
    for key in selected_coffee_type:
        if key != 'money':
            total_resources[key] -= selected_coffee_type[key]
        else:
            total_resources["profit"] += selected_coffee_type["money"]


def show_report():
    for key in total_resources:
        resource = ''
        if key == 'water' or key == 'milk':
            resource = f"{total_resources[key]}ml"
        elif key == 'sugar' or key == 'chocolate' or key == 'coffee':
            resource = f"{total_resources[key]}gr"
        elif key == 'profit':
            resource = f"${total_resources['profit']}"

        print(f"{key.title()}: {resource}")


def coffee_machine():
    coffees = {
        "espresso": {
            "water": 200,
            "sugar": 25,
            "coffee": 75,
            "money": 2.5
        },

        "latte": {
            "water": 150,
            "milk": 50,
            "sugar": 25,
            "coffee": 75,
            "money": 2.75
        },

        "cappuccino": {
            "water": 200,
            "sugar": 25,
            "chocolate": 30,
            "coffee": 75,
            "money": 3.00
        },
    }

    machine_on = True

    while machine_on:

        coffee_type = select_coffee_type()

        if coffee_type == 'off':
            machine_on = False
        elif coffee_type == 'report':
            show_report()
        elif coffee_type != 'espresso' and coffee_type != 'latte' and coffee_type != 'cappuccino':
            print("Selected type is invalid. Please try again.")
        else:
            selected_coffee = coffees[coffee_type]

            missing_resource = check_resources(selected_coffee)

            if missing_resource is not False:
                print(f"Sorry there is not enough {missing_resource}")
            else:
                coin_inserter = CoinInserter()
                print("Please insert coins")
                coin_inserter.mainloop()

                total_money = coin_inserter.get_total_money()
                print(f'Total money inserted: ${total_money: .2f}')

                if total_money < selected_coffee['money']:
                    print("Sorry that's not enough money. Money refunded.")
                elif total_money > selected_coffee["money"]:
                    print(f"""Here is ${
                    (selected_coffee['money'] - total_money) * -1} dollars in change and your {coffee_type.title()}, enjoy!.""")
                    update_resources(selected_coffee)
                else:
                    update_resources(selected_coffee)
                    print(f"Here is your {coffee_type.title()}. Enjoy!")


coffee_machine()
