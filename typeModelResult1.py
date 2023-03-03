import tensorflow as tf
import numpy as np
import json

# Define the input data shape
input_data_shape = (None, 32) # This allows the input shape to be flexible, as the number of entries will vary

# Define the model architecture
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(32, activation='relu', input_shape=input_data_shape),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(5, activation='softmax') # We have 3 transaction types
])

# Compile the model
model.compile(optimizer=tf.keras.optimizers.Adam(0.001), loss='categorical_crossentropy', metrics=['accuracy'])


#json data




# Define the data for the AI to learn from

transaction_data = np.array([[0, 33000000, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1424401, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
[0, 7159300, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1424402, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
[0, 500000, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1424402, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
[0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1424418, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
[0, 12000000, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1424418, 0, 0, 0, 0, 6658, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0]
    ])


#FUNCITONINGLABELS
transaction_labels = np.array([[0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0]]) # These are e are the labels for the transaction types from transactionEncoding.py

model.fit(transaction_data, transaction_labels, epochs=90)

#from transaction Encoding.py
new_transaction = np.array([[0, 10000000, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1424422, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]]) # This is a new transaction

#this successfully predicts the type for the frist resutl from this transaction as exit
prediction = model.predict(new_transaction)
print(prediction)

#this is the encoded result from the fed result encodeResultData.py
print([0.0, 0.0, 1.0, 0.0, 0.0])
