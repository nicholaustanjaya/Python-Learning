# Write favorite foods
with open("foods.txt", "w") as file:
    for i in range(3):
        food = input(f"Enter favorite food #{i+1}: ")
        file.write(food + "\n")

# Read and display
with open("foods.txt", "r") as file:
    foods = file.read()
    print("Your favorite foods are:")
    print(foods)