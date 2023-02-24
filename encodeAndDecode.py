import numpy as np
import json
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

unique_asset_buckets = list(set(assetBuckets))
print(unique_asset_buckets)

unique_types = list(set(types))
print(unique_types)

# Encode the 'Type' and 'assetBucket' fields using one-hot encoding
label_encoder_type = LabelEncoder()
integer_encoded_type = label_encoder_type.fit_transform(unique_types)
onehot_encoder_type = OneHotEncoder(sparse=False, handle_unknown='ignore')
integer_encoded_type = integer_encoded_type.reshape(len(integer_encoded_type), 1)
onehot_encoded_type = onehot_encoder_type.fit_transform(integer_encoded_type)

label_encoder_bucket = LabelEncoder()
integer_encoded_bucket = label_encoder_bucket.fit_transform(unique_asset_buckets)
onehot_encoder_bucket = OneHotEncoder(sparse=False, handle_unknown='ignore')
integer_encoded_bucket = integer_encoded_bucket.reshape(len(integer_encoded_bucket), 1)
onehot_encoded_bucket = onehot_encoder_bucket.fit_transform(integer_encoded_bucket)

#print(types)
#print(assetBuckets)
print(onehot_encoded_type)
print(onehot_encoded_bucket)



max_indices1 = np.argmax(onehot_encoded_type, axis=1)
max_indices2 = np.argmax(onehot_encoded_bucket, axis=1)

# Get the inverse mapping of integer-encoded values to original string values
inverse_mapping_type = label_encoder_type.inverse_transform(range(len(label_encoder_type.classes_)))
inverse_mapping_bucket = label_encoder_bucket.inverse_transform(range(len(label_encoder_bucket.classes_)))

# Replace unknown integer-encoded values with the string 'unknown'
unknown_indices_type = set(max_indices1) - set(integer_encoded_type.flatten())
for index in unknown_indices_type:
    max_indices1[max_indices1 == index] = len(label_encoder_type.classes_)

unknown_indices_bucket = set(max_indices2) - set(integer_encoded_bucket.flatten())
for index in unknown_indices_bucket:
    max_indices2[max_indices2 == index] = len(label_encoder_bucket.classes_)

# Convert the integer-encoded values back to the original string values
decoded_type = inverse_mapping_type[max_indices1]
decoded_bucket = inverse_mapping_bucket[max_indices2]

print(decoded_type)
print(decoded_bucket)
