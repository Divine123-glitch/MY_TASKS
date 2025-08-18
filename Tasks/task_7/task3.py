#   Days and Activities Pairing


# Store days of the week  in a tuple
days = ("Monday", "Tuseday" "Wednesday","Thursday", "Friday")

# Step 2: Ask user for activities
activities = []
for day in days:
    activity = input(f"Enter an activity for {day}: ")
    activities.append(activity)

# Pair days with activities using zip() 
schedule = {day: activity for day, activity in zip(days, activities)}


print("--- Days and Activities ---")
print(schedule)
