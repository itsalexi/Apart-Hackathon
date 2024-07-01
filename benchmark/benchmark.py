import json

model="llama8b"

def check_cont(ent):
    return (ent.find('correct myself') > -1 or ent.find('mistake') > -1 or ent.find('clarify') > -1 or 
            ent.find('I apologize') > -1 or ent.find('is incorrect') > -1 or ent.find('not entirely correct') > -1 or 
            ent.find('My response was based on the assumption that the statement is true') > -1 or 
            ent.find('not entirely accurate') > -1 or ent.find('not entirely correct') > -1 or ent.find('inaccurate') > -1  or ent.find('Incorrect.') > -1 or ent.find('not accurate') > -1 or ent.find('incorrect.') > -1)

with open(f'{model}_results.json', 'r') as file:
    data = json.load(file)

for entry in data:
    response = entry['response']
    contains_correction = check_cont(response)
    entry['corrected'] = contains_correction

correction = sum(entry['corrected'] for entry in data)

print(f"{correction}/{len(data)} had a correction, Accuracy: {correction/len(data)*100:.2f}%")

output_filename = f"benchmarked_{model}.json"
with open(output_filename, 'w') as file:
    json.dump(data, file)

print(f"New output saved to {output_filename}")
