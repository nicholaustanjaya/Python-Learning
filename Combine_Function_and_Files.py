def analyze_scores(scores):
    average = sum(scores) / len(scores)
    highest = max(scores)
    lowest = min(scores)
    return average, highest, lowest

with open("scores.txt", "w") as file:
    for i in range(5):
        score = input(f"Enter score #{i+1}: ")
        file.write(score + "\n")

with open("scores.txt", "r") as file:
    lines = file.readlines()
    scores = [int(line.strip()) for line in lines]

avg, high, low = analyze_scores(scores)
print(f"Average: {avg}")
print(f"Highest: {high}")
print(f"Lowest: {low}")
