import os


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


auctions = {}
end_program = False
top_auction = ["", 0]

print("Welcome to the secret auction program")

while not end_program:
    name = input("What is your name? ")

    while not name.isalpha():
        name = input("Please write a valid name ")

    while True:
        try:
            bid = int(input("What's your bid? $"))
            break
        except ValueError:
            print("Invalid characters, please provide numbers.")

    auctions[name] = bid

    while True:
        more_people = input(
            "Are there more auctioners? type 'yes' or 'no' ").lower()
        if more_people != 'yes' and more_people != 'no':
            more_people = input(
                "Please type a correct answer, remember only 'yes' and 'no' values are accepted ").lower()
        else:
            break

    if more_people == 'yes':
        clear_console()
    else:
        end_program = True


for key in auctions:
    if auctions[key] > top_auction[1]:
        top_auction = [key, auctions[key]]

print(auctions)

print(f"The winner is {top_auction[0]} with a bid of {top_auction[1]}")
