# Football Match Ticket System

# Store all seat number in a set
seat_number = set(range(1, 51))

# Ask users to book a seat number
booked_seat = int(input("Enter a seat number between (1-50): "))
seat_number.remove(booked_seat)
print(f"You have sucessfully booked seat number", booked_seat)

# Print remaining seats
print(f"Remainig seats: ", seat_number)