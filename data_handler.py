import json
import os

DATA_FILE = "data.json"

def load_data():
    """Load data from a JSON file."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            data = json.load(file)
    else:
        # Default data structure
        data = {
            "weekly_outings": [0, 0, 0, 0],
            "weekly_spending": [0.0, 0.0, 0.0, 0.0],
            "charges": [[], [], [], []],  # Charges per week
            "monthly_budget": 300.0
        }

    # Ensure all keys exist in the loaded data
    if "weekly_outings" not in data:
        data["weekly_outings"] = [0, 0, 0, 0]
    if "weekly_spending" not in data:
        data["weekly_spending"] = [0.0, 0.0, 0.0, 0.0]
    if "charges" not in data:
        data["charges"] = [[], [], [], []]
    if "monthly_budget" not in data:
        data["monthly_budget"] = 300.0

    return data

def save_data(data):
    """Save data to a JSON file."""
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

def log_charge(data, week, charge_name, charge_amount):
    """Log a charge for a specific week."""
    data["charges"][week].append({"name": charge_name, "amount": charge_amount})
    data["weekly_spending"][week] += charge_amount
    save_data(data)
