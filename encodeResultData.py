import numpy as np
import json
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

# Load the JSON data from a file
#with open('trainingSet1Result.json', 'r') as f:
#    json_data = json.load(f)

json_data = [{
                "blockLevel": 1424401,
                "Type": "entry",
                "Value": 33, 
                "Alias": "XTZ transfer",
                "assetBucket": "XTZ"
        },
        {
                "blockLevel": 1424402,
                "Type": "exit",
                "Value": -7,
                "Alias": "taco buy",
                "assetBucket": "XTZ"
        },
        {
                "blockLevel": 1424402,
                "Type": "FMV",
                "Value": 0.5,
                "Alias": "taco return",
                "assetBucket": "XTZ"
        
        },
        {
                "blockLevel": 1424402,
                "Type": "entry",
                "Value": 1,
                "Alias": "taco buy",
                "assetBucket": "TacoHolder1"
        
        },

  
        {
                "blockLevel": 1424418,
                "Type": "non-value communication",
                "Value": 0,
                "Alias": "taco bucket update op",
                "assetBucket": "TacoHolder1"
        },
        
        {
                "blockLevel": 1424418,
                "Type": "value communication",
                "Value": -1.2,
                "Alias": "config taco auction",
                "assetBucket": "XTZ"
        },
        {
                "blockLevel": 1424418,
                "Type": "value communication",
                "Value": 1.2,
                "Alias": "config taco auction",
                "assetBucket": "XTZ"
        },
        
        {
                "blockLevel": 1424418,
                "Type": "non-value communication",
                "Value": 0,
                "Alias": "config taco for auction",
                "assetBucket": "TacoHolder1"
        },
        {
                "blockLevel": 1424422,
                "Type": "exit",
                "Value": -10,
                "Alias": "swapRSAL from XTZ",
                "assetBucket": "XTZ"
        },
   {
                "blockLevel": 1424422,
                "Type": "entry",
                "Value": 5880,
        "Alias": "swapRSAL from XTZ",
                "assetBucket": "RSAL"
        }
]
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

# Create a new array to store the encoded data
# Create the encoded data array
encoded_data = []
for i in range(len(blockLevels)):
    # Encode the type and assetBucket values for this element
    type_index = unique_types.index(types[i])
    bucket_index = unique_asset_buckets.index(assetBuckets[i])
    type_encoding = onehot_encoded_type[type_index].tolist()
    bucket_encoding = onehot_encoded_bucket[bucket_index].tolist()
    
    # Add the blockLevel, value, type, and assetBucket to a new subarray
    subarray = [blockLevels[i], values[i], type_encoding, bucket_encoding]
    
    # Append the subarray to the encoded_data array
    encoded_data.append(subarray)

# Decode the last element of the encoded_data array
decoded_blockLevel = encoded_data[-1][0]
decoded_value = encoded_data[-1][1]
decoded_type_index = onehot_encoded_type.tolist().index(encoded_data[-1][2])
decoded_type = unique_types[decoded_type_index]
decoded_bucket_index = onehot_encoded_bucket.tolist().index(encoded_data[-1][3])
decoded_bucket = unique_asset_buckets[decoded_bucket_index]

print("Encoded data:")
print(encoded_data)
print("Decoded last element:")
print(f"blockLevel: {decoded_blockLevel}, value: {decoded_value}, Type: {decoded_type}, assetBucket: {decoded_bucket}")
