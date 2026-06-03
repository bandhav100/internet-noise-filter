import json
import matplotlib.pyplot as plt

# Load trend scores
with open("outputs/trend_scores.json", "r") as file:
    trend_scores = json.load(file)

# Extract labels and values
labels = list(trend_scores.keys())
values = list(trend_scores.values())

# Create figure
plt.figure(figsize=(10, 6))

# Bar chart
plt.bar(labels, values)

# Titles
plt.title("Technology Trend Intelligence")
plt.xlabel("Trend Categories")
plt.ylabel("Trend Score")

# Add values on top of bars
for i, value in enumerate(values):
    plt.text(i, value + 0.5, str(value), ha="center")

# Save chart
plt.savefig("outputs/trend_chart.png")

# Show chart
plt.show()

print("Chart saved: outputs/trend_chart.png")
