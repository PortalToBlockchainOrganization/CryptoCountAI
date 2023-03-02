def flatten_dict(d, prefix=''):
    """
    A recursive function that flattens a nested dictionary.

    Parameters:
        - d (dict): The dictionary to flatten.
        - prefix (str): A string to add to the beginning of each flattened key.

    Returns:
        - dict: A dictionary with flattened keys.
    """
    items = []
    for k, v in d.items():
        new_prefix = prefix + k + '_'
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_prefix).items())
        else:
            items.append((new_prefix[:-1], v))
    return dict(items)

def get_unique_keys(transactions):
    """
    Given an array of dictionaries, returns a set of all unique keys across all dictionaries.

    Parameters:
        - transactions (list): An array of dictionaries.

    Returns:
        - set: A set of all unique keys across all dictionaries.
    """
    keys = set()
    for tx in transactions:
        for k in tx.keys():
            keys.add(k)
    return keys
def encode_transactions(transactions):
    """
    Encodes an array of dictionaries as a 2D array, where each row corresponds to a dictionary and
    each column corresponds to a unique key across all dictionaries.

    Parameters:
        - transactions (list): An array of dictionaries.

    Returns:
        - list: A 2D array, where each row corresponds to a dictionary and each column corresponds to a
                unique key across all dictionaries.
    """
    # Get set of unique keys across all dictionaries
    keys = get_unique_keys(transactions)

    # Initialize output array
    output_arr = []

    # Encode each dictionary as a row in the output array
    for tx in transactions:
        row = []
        flattened_tx = flatten_dict(tx)
        for k in keys:
            if k in flattened_tx:
                row.append(flattened_tx[k])
            else:
                row.append(0)
        output_arr.append(row)

    return output_arr
trans = [{
        "level": 1424401,
        "sender": 1,
        "senderAddress": "tz1T9jPnGshxF4UKPDwS2QivVsonkZVkssBr",
        "target": 1,
        "targetAddress": "tz1Yah7WCq8p3z2Qi4kp52FcDik9j7sUZMVN",
        "amount": 33000000
    },
    {
    "level": 1424402,
    "sender": 1,
    "senderAddress": "tz1Yah7WCq8p3z2Qi4kp52FcDik9j7sUZMVN",
    "target": 1,
    "targetAlias": "TzTacos V3",
    "targetAddress": "KT1JYWuC4eWqYkNC1Sh6BiD89vZzytVoV2Ae",
    "amount": 7159300,
    "parameter": 1,
    "parameterEntrypoint": "buyTaco",
    "parameterValue":  0
    }]

value = encode_transactions(trans)
print(value)
