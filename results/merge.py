import json
import glob

model = ''
directory = './results/' + model + '/'
merged_array = []

json_files = glob.glob(directory + '*.json')

for file in json_files:
    with open(file) as f:
        data = json.load(f)
    
    merged_array.extend(data)
    output_file = directory + f'{model}.json'
    with open(output_file, 'w') as f:
        json.dump(merged_array, f)