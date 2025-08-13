# Tuple Unpacking


# Ask user for inputs
Data = ([
            input("Enter first name: "),
            input("Enter Age: "),
            input("Enter favourite color: "),
            input("Enter home town: "),
])


# Unpack variables
Name = (Data[0])
Age = (Data[1])
Color = (Data[2])
Town = (Data[3])


# Print and use  escape sequence to align each piece of information nicely.
print(f"{Name}\t {Age}\t {Color}\t {Town}")