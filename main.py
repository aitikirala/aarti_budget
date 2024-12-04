from budget_calculator import calculate_dynamic_weekly_budget
from savings_suggestions import suggest_savings
from data_handler import load_data, save_data, log_charge

# Load persistent data
data = load_data()
monthly_budget = data["monthly_budget"]
weekly_outings = data["weekly_outings"]
weekly_spending = data["weekly_spending"]

def log_charge_ui():
    """Log a charge for a specific week."""
    week = int(input("Enter the week number (1-4): ")) - 1
    if 0 <= week < 4:
        charge_name = input("Enter the name of the charge: ")
        charge_amount = float(input(f"Enter the price for {charge_name}: $"))
        log_charge(data, week, charge_name, charge_amount)
        print(f"Logged {charge_name} for ${charge_amount:.2f}. Remaining budget for Week {week + 1}: ${calculate_remaining_budget(week):.2f}")
    else:
        print("Invalid week number.")

def calculate_remaining_budget(week):
    """Calculate the remaining budget for the current week."""
    weekly_budgets = calculate_dynamic_weekly_budget(monthly_budget, weekly_outings)
    return weekly_budgets[week] - weekly_spending[week]

def main():
    """Main program loop."""
    while True:
        print("\nMenu:")
        print("1. Enter outings for the week (Sunday update).")
        print("2. Log a charge for a specific week.")
        print("3. Edit outings or spending.")
        print("4. View weekly budgets and suggestions.")
        print("5. Exit.")

        choice = input("Choose an option: ")

        if choice == "1":
            for week in range(4):
                weekly_outings[week] = int(input(f"Enter outings for Week {week + 1}: "))
            save_data(data)
            print("Outings updated.")
        elif choice == "2":
            log_charge_ui()
        elif choice == "3":
            sub_choice = input("Edit (1) outings or (2) spending? ")
            if sub_choice == "1":
                week = int(input("Enter the week number (1-4): ")) - 1
                if 0 <= week < 4:
                    new_outings = int(input(f"Enter new outings for Week {week + 1}: "))
                    weekly_outings[week] = new_outings
                    save_data(data)
                    print(f"Week {week + 1} outings updated to {new_outings}.")
                else:
                    print("Invalid week number.")
            elif sub_choice == "2":
                week = int(input("Enter the week number (1-4): ")) - 1
                if 0 <= week < 4:
                    new_spending = float(input(f"Enter new spending for Week {week + 1}: "))
                    weekly_spending[week] = new_spending
                    save_data(data)
                    print(f"Week {week + 1} spending updated to ${new_spending:.2f}.")
                else:
                    print("Invalid week number.")
            else:
                print("Invalid choice.")
        elif choice == "4":
            weekly_budgets = calculate_dynamic_weekly_budget(monthly_budget, weekly_outings)
            for week in range(4):
                print(f"\nWeek {week + 1}:")
                print(f"  Budget: ${weekly_budgets[week]:.2f}")
                print(f"  Spending: ${weekly_spending[week]:.2f}")
                remaining_budget = calculate_remaining_budget(week)
                print(f"  Remaining Budget: ${remaining_budget:.2f}")
                print(suggest_savings(weekly_budgets, weekly_spending, week))
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
