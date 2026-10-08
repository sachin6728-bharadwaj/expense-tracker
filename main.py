# Personal Expense Tracker
# Tracks money spent, category wise and day wise.
# Data lives in a list while the program runs.

categories = ["food", "travel", "books", "entertainment", "other"]
expenses = []  # each expense is a tuple -> (day, category, amount, note)
budget = 0.0


def show_menu():
    options = ["Set monthly budget", "Add expense", "View all expenses",
               "Category wise total", "Top 3 expenses",
               "Day wise report", "Budget status", "Exit"]

    print("\n===== EXPENSE TRACKER =====")
    for i in range(len(options)):
        print(str(i + 1) + ". " + options[i])


def read_number(message):
    # keeps asking till the user types a valid positive number
    while True:
        try:
            num = float(input(message))
        except ValueError:
            print("Please enter a number only.")
            continue

        if num > 0:
            return num

        print("Number should be greater than 0.")


def total_spent():
    total = 0
    for e in expenses:
        total = total + e[2]
    return total


def no_data():
    if len(expenses) == 0:
        print("No expenses yet.")
        return True
    return False


def set_budget():
    global budget
    budget = read_number("Enter monthly budget: ")
    print("Budget set to", budget)


def add_expense():
    day = int(read_number("Day of the month (1-31): "))

    print("Categories:")
    for i in range(len(categories)):
        print(i + 1, "-", categories[i])

    choice = int(read_number("Choose category number: "))

    if day > 31 or choice > len(categories):
        print("Invalid day or category, expense not added.")
        return

    amount = read_number("Amount spent: ")
    note = input("Short note: ")

    expenses.append((day, categories[choice - 1], amount, note))
    print("Expense added.")


def view_all():
    if no_data():
        return

    print("\nDay  Category        Amount      Note")
    print("-" * 45)

    for e in expenses:
        print(
            str(e[0]).ljust(5)
            + e[1].ljust(16)
            + str(e[2]).ljust(10)
            + e[3]
        )

    print("-" * 45)
    print("Total spent:", total_spent())


def category_totals():
    if no_data():
        return

    totals = {}

    for c in categories:
        totals[c] = 0

    for e in expenses:
        totals[e[1]] += e[2]

    grand = total_spent()

    print("\nCategory wise spending")

    for c in totals:
        percent = totals[c] / grand * 100
        print(c.ljust(15), str(totals[c]).ljust(10), round(percent, 1), "%")


def top_three():
    if no_data():
        return

    temp = expenses[:]  # copy, so the original order is not disturbed
    n = len(temp)
    limit = min(3, n)

    # selection sort, only the first 3 positions are needed
    for i in range(limit):
        max_pos = i

        for j in range(i + 1, n):
            if temp[j][2] > temp[max_pos][2]:
                max_pos = j

        t = temp[i]          # exchange
        temp[i] = temp[max_pos]
        temp[max_pos] = t

    print("\nTop expenses")

    for i in range(limit):
        print(str(i + 1) + ". " + temp[i][3] + " - " + str(temp[i][2]))


def day_report():
    if no_data():
        return

    daily = {}

    for e in expenses:
        if e[0] in daily:
            daily[e[0]] += e[2]
        else:
            daily[e[0]] = e[2]

    days = list(daily.keys())
    days.sort()

    print("\nDay wise spending")

    for d in days:
        print("Day", d, ":", daily[d])


def budget_status():
    if budget == 0:
        print("Set a budget first (option 1).")
        return

    spent = total_spent()
    used = spent / budget * 100

    print("\nBudget:", budget, "| Spent:", spent)

    if spent <= budget:
        print("Remaining:", budget - spent)
    else:
        print("Over budget by:", spent - budget)

    print("Budget used:", round(used, 1), "%")

    if used >= 100:
        print("You have crossed your budget!")
    else:
        print("You are doing fine.")


def main():
    print("Welcome to the Expense Tracker!")

    while True:
        show_menu()

        choice = input("Enter your choice: ")

        if choice == "1":
            set_budget()

        elif choice == "2":
            add_expense()

        elif choice == "3":
            view_all()

        elif choice == "4":
            category_totals()

        elif choice == "5":
            top_three()

        elif choice == "6":
            day_report()

        elif choice == "7":
            budget_status()

        elif choice == "8":
            print("Bye, spend wisely!")
            break

        else:
            print("Wrong choice, try again.")


main()