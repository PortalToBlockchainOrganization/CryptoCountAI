import tensorflow as tf
import numpy as np
import json

# Define the input data shape
input_data_shape = (None, 10) # This allows the input shape to be flexible, as the number of entries will vary

# Define the model architecture
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(32, activation='relu', input_shape=input_data_shape),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(3, activation='softmax') # We have 3 transaction types
])

# Compile the model
model.compile(optimizer=tf.keras.optimizers.Adam(0.001), loss='categorical_crossentropy', metrics=['accuracy'])


#json data
with open('trainingSet1.json', 'r') as f:
    json_data1 = json.load(f)
    array1 = np.array(json_data1)

# Load the second JSON file and convert to numpy array
with open('trainingSet1Result.json', 'r') as f:
    json_data2 = json.load(f)
    array2 = np.array(json_data2)

# Print the arrays
print(array1)
print(array2)




# Define the data for the AI to learn from
transaction_data = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                            [11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
                            [21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
                            [31, 32, 33, 34, 35, 36, 37, 38, 39, 40]]) # This is sample transaction data
transaction_labels = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1], [0, 0, 1]]) # These are the labels for the transaction types

# Train the model on the data
#model.fit(transaction_data, transaction_labels, epochs=10)
model.fit(array1, array2, epochs=20)


# Use the model to make predictions on new data
#new_transaction = np.array([[41, 42, 43, 44, 45, 46, 47, 48, 49, 50]]) # This is a new transaction
#import new transaction
with open('nextTransaction.json', 'r') as f:
    json_data3 = json.load(f)
    array3 = np.array(json_data3)



prediction = model.predict(array3)
print(prediction)
