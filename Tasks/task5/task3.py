# Tuple Operations


# Ask user for name of five different states
state = [
            input("Enter first state: "),
            input("Enter second state name: "),
            input("Enter third state name: "),
            input("Enter fourth state name: "),
            input("Enter fifth state name: "),
]


# Convert to tuple
states = tuple(state)

# print first state and last state
print(states[0])
print(states[-1])

# Check if "Lagos" is in the tuple and print "Yes" or "No"
print("Lagos" in states)

# Print the number of states entered
print(len(states))