# Constants
COACH_COSTS = {
    "12-16": {"hire": 150, "meal": 14.00, "ticket": 21.00},
    "17-26": {"hire": 190, "meal": 13.50, "ticket": 20.00},
    "27-39": {"hire": 225, "meal": 13.00, "ticket": 19.00}
}
MIN_SENIORS = 10
MAX_SENIORS = 36
MIN_CARERS = 2
EXTRA_CARERS_THRESHOLD = 24
CARER_COST = 0

# Function to calculate the outing costs
def calculate_outing_cost(num_seniors):
    if num_seniors < MIN_SENIORS or num_seniors > MAX_SENIORS:
        return None, None

    if num_seniors > EXTRA_CARERS_THRESHOLD:
        num_carers = MIN_CARERS + 1
    else:
        num_carers = MIN_CARERS

    senior_cost = COACH_COSTS["12-16"]["hire"] + COACH_COSTS["12-16"]["meal"] + COACH_COSTS["12-16"]["ticket"]
    total_cost = senior_cost * num_seniors + num_carers * CARER_COST

    return total_cost, total_cost / (num_seniors + num_carers)

# Function to record participants and payments
def record_outing_participants(num_seniors, total_cost):
    participants = []
    total_payment = 0

    for i in range(num_seniors):
        name = input(f"Enter name of senior citizen {i+1}: ")
        payment = float(input(f"Enter amount paid by {name}: "))
        participants.append((name, payment))
        total_payment += payment

    return participants, total_payment

# Function to determine break-even point or profit
def calculate_profit(total_cost, total_payment):
    if total_payment >= total_cost:
        return "Break-even"
    else:
        return f"Profit of ${total_cost - total_payment:.2f}"

# Main program
def main():
    num_seniors = int(input("Enter the number of senior citizens interested in the outing: "))

    total_cost, cost_per_person = calculate_outing_cost(num_seniors)
    if total_cost is None:
        print("Invalid number of senior citizens.")
        return

    print(f"Total cost for the outing: ${total_cost:.2f}")
    print(f"Cost per person: ${cost_per_person:.2f}")

    participants, total_payment = record_outing_participants(num_seniors, total_cost)
    print("\nList of participants:")
    for participant, payment in participants:
        print(f"{participant}: ${payment:.2f}")

    print(f"\nTotal amount collected: ${total_payment:.2f}")

    profit_or_break_even = calculate_profit(total_cost, total_payment)
    print(f"\nProfit/Loss: {profit_or_break_even}")

if __name__ == "__main__":
    main()
