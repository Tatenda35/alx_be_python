# daily_reminder.py

def main():
    # Loop to ensure non-empty task input
    while True:
        task = input("Enter your task: ").strip()
        if task:
            break
        print("Task cannot be empty. Please enter a valid task.")

    # Loop to ensure valid priority input
    while True:
        priority = input("Priority (high/medium/low): ").strip().lower()
        if priority in ("high", "medium", "low"):
            break
        print("Invalid priority. Please enter 'high', 'medium', or 'low'.")

    # Loop to ensure valid time-bound input
    while True:
        time_bound = input("Is it time-bound? (yes/no): ").strip().lower()
        if time_bound in ("yes", "no"):
            break
        print("Invalid input. Please enter 'yes' or 'no'.")

    # Use match case for priority response
    match priority:
        case "high":
            reminder = f"'{task}' is a high priority task"
        case "medium":
            reminder = f"'{task}' is a medium priority task"
        case "low":
            reminder = f"'{task}' is a low priority task"

    # Append message based on time-bound status
    if time_bound == "yes":
        reminder += " that requires immediate attention today!"
    else:
        reminder = "Note: " + reminder + ". Consider completing it when you have free time."

    print("\nReminder:", reminder)
    print("\nWell done on completing this project! Let the world hear about this milestone achieved.")
    print("🚀 Click here to tweet! 🚀")

if __name__ == "__main__":
    main()

