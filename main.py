expenses = []

def removeExpense():
    while True:
        listExpenses()
        print("What expense would you like to remove?")
        try:
            expenseToRemove = int(input("> "))
            if 0 <= expenseToRemove < len(expenses):
                del expenses[expenseToRemove]
                break
            else:
                print("Invalid index. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def addExpense(amount, category):
    expense = {'amount': float(amount), 'category': category}
    expenses.append(expense)

def printMenu():
    print("\nPlease choose from one of the following options...")
    print("1. Add A New Expense")
    print("2. Remove An Expense")
    print("3. List All Expenses")
    print("4. View Monthly Summary")
    print("5. View Category-wise Expenditure")
    print("6. Exit")

def listExpenses():
    print("\nHere is a list of your expenses...")
    print("------------------------------------")
    for idx, expense in enumerate(expenses):
        print(f"#{idx} - ${expense['amount']} - {expense['category']}")
    print("\n")

def viewMonthlySummary():
    total = sum(expense['amount'] for expense in expenses)
    print(f"\nTotal monthly expenses: ${total:.2f}\n")

def viewCategoryWiseExpenditure():
    categories = {}
    for expense in expenses:
        if expense['category'] in categories:
            categories[expense['category']] += expense['amount']
        else:
            categories[expense['category']] = expense['amount']

    print("\nCategory-wise expenditure:")
    print("---------------------------")
    for category, amount in categories.items():
        print(f"{category}: ${amount:.2f}")
    print("\n")

def getCategoryInput():
    print("Please select a category for the expense:")
    print("1. Food")
    print("2. Transportation")
    print("3. Entertainment")
    print("4. Other")
    while True:
        try:
            categoryOption = int(input("> "))
            if categoryOption == 1:
                return "Food"
            elif categoryOption == 2:
                return "Transportation"
            elif categoryOption == 3:
                return "Entertainment"
            elif categoryOption == 4:
                return "Other"
            else:
                print("Invalid option. Please select a valid category.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    while True:
        printMenu()
        optionSelected = input("> ")

        if optionSelected == "1":
            print("How much was this expense?")
            while True:
                try:
                    amountToAdd = float(input("> "))
                    break
                except ValueError:
                    print("Invalid input. Please enter a number.")

            category = getCategoryInput()
            addExpense(amountToAdd, category)
        elif optionSelected == "2":
            removeExpense()
        elif optionSelected == "3":
            listExpenses()
        elif optionSelected == "4":
            viewMonthlySummary()
        elif optionSelected == "5":
            viewCategoryWiseExpenditure()
        elif optionSelected == "6":
            print("Exiting the expense tracker. Goodbye!")
            break
        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()
