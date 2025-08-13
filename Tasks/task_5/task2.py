# Tuple and Input
# Ask user for five best friends names
Friend = [
            input("Enter first best friend name: "),
            input("Enter second best friend name: "),
            input("Enter third best friend name: "),
            input("Enter fourth best friend name: "),
            input("Enter fifth best friend name: "),
]

# Store in a tuple
Friends = tuple(Friend)

# Print tuple in reverse order
print(Friends[::-1])