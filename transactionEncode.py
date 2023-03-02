from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder

#output from organizetransactionsByLenght.py

# input array
input_arr = [[0, 'tz1T9jPnGshxF4UKPDwS2QivVsonkZVkssBr', 33000000, 1, 'tz1Yah7WCq8p3z2Qi4kp52FcDik9j7sUZMVN', 0, 1424401, 0, 1, 0], [1, 'tz1Yah7WCq8p3z2Qi4kp52FcDik9j7sUZMVN', 715>
# initialize LabelEncoder
le = LabelEncoder()

# iterate over each sub-array in input_arr
for i in range(len(input_arr)):
    # iterate over each element in sub-array
    for j in range(len(input_arr[i])):
        # if the element is a string, encode it using LabelEncoder
        if isinstance(input_arr[i][j], str):
            input_arr[i][j] = le.fit_transform([input_arr[i][j]])[0]

print(input_arr)

