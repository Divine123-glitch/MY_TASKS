# List Manipulation**
# Step 1: Create a list of five cities.
# Step 2: Replace the third city with a new one (entered by the user).
# Step 3: Remove the last city.
# Step 4: Add a new city to the beginning of the list.
# Step 5: Print the updated list.

Cities = ["Auchi", "Aba", "Abeokuta", "Akure", "Adamawa"]
new_city = input("Enter a new city for third position: ")
Cities[2] = new_city
Cities.remove("Adamawa")
print(Cities)
Cities.insert(0, "Lagos")
print(Cities)

