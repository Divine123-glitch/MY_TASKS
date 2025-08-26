# Days and Activities Pairing

# Store days of the week in a tuple (corrected typo)
days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")

# Collect activities with exception handling
activities = []
try:
    for day in days:
        activity = input(f"Enter an activity for {day}: ").strip()
        if not activity:
            raise ValueError(f"Activity for {day} cannot be empty")
        activities.append(activity)

except ValueError as e:
    print(f"Error: {e}")
    exit(1)
except KeyboardInterrupt:
    print("\nProgram terminated by user.")
    exit(0)

# Pair days with activities using zip()
schedule = {day: activity for day, activity in zip(days, activities)}

# Print formatted output
print("--- Days and Activities ---")
print(schedule)