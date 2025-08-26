# Name Organizer
# Step 1: Ask user for 5 names
# Step 2: Convert to lowercase
# Step 3: Sort the list
# Step 4: Print result

try:
    names_input = input("Enter 5 names (separated by spaces): ").strip()
    if not names_input:
        raise ValueError("Input cannot be empty or just whitespace")

    names = [name.strip().lower() for name in names_input.split()]
    if len(names) != 5:
        raise ValueError("Exactly 5 names must be provided")
    if any(not name for name in names):
        raise ValueError("No name can be empty")

    names.sort()

    print("\n--- Sorted Names ---")
    for name in names:
        print(name)

except ValueError as e:
    print(f"Error: {e}")
    exit(1)
except KeyboardInterrupt:
    print("\nProgram terminated by user.")
    exit(0)