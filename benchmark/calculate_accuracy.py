import json
model = "gemma-7b"

with open(f'benchmarked_{model}.json', 'r') as file:
    data = json.load(file)
    
# Initialize counters
total_correct = 0
total_responses = len(data)
topic_counts = {}
topic_correct_counts = {}

# Calculate counts and correct counts per topic
for entry in data:
    topic = entry["topic"]
    if topic in topic_counts:
        topic_counts[topic] += 1
    else:
        topic_counts[topic] = 1
    
    if entry["corrected"]:
        total_correct += 1
        if topic in topic_correct_counts:
            topic_correct_counts[topic] += 1
        else:
            topic_correct_counts[topic] = 1

# Calculate overall accuracy
overall_accuracy = (total_correct / total_responses) * 100

# Calculate accuracy per topic
topic_accuracies = {}
for topic in topic_counts:
    if topic in topic_correct_counts:
        accuracy = (topic_correct_counts[topic] / topic_counts[topic]) * 100
        topic_accuracies[topic] = accuracy
    else:
        topic_accuracies[topic] = 0.0  # No correct entries in this topic

# Print results
print(f"Overall Accuracy: {overall_accuracy:.2f}%")
print("Accuracy per Topic:")
for topic, accuracy in topic_accuracies.items():
    print(f"- {topic}: {accuracy:.2f}%")