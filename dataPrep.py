import json
import numpy as np
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

# Load the JSON data from a file
with open('trainingSet1Result.json', 'r') as f:
    json_data = json.load(f)

# Extract the values for each field
blockLevels = [item['blockLevel'] for item in json_data]
types = [item['Type'] for item in json_data]
values = [item['Value'] for item in json_data]
aliases = [item['Alias'] for item in json_data]
assetBuckets = [item['assetBucket'] for item in json_data]

# Encode the 'Type' field using one-hot encoding
label_encoder = LabelEncoder()
integer_encoded = label_encoder.fit_transform(types)
onehot_encoder = OneHotEncoder(sparse=False)
integer_encoded = integer_encoded.reshape(len(integer_encoded), 1)
onehot_encoded = onehot_encoder.fit_transform(integer_encoded)

# Combine all the fields into a single numpy array
data = np.column_stack((blockLevels, values, aliases, assetBuckets, onehot_encoded))

# Print the final numpy array
print(data)
