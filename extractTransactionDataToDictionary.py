import json
# load the data
with open('trainingSet1Cleaned.json', 'r') as f:
    json_data = json.load(f)

transactions = []
for item in json_data:
    transaction = {
        'level': item['level'],
        'sender_address': item['sender'].get('address'),
        'sender_alias': item['sender'].get('alias'),
        'target_address': item['target'].get('address'),
        'target_alias': item['target'].get('alias'),
        'amount': item['amount'],
        'parameter_entrypoint': item.get('parameter', {}).get('entrypoint'),
        'parameter_value': item.get('parameter', {}).get('value')
    }
    
    if transaction['parameter_entrypoint'] == 'configure':
        asset = transaction['parameter_value']['asset'][0]
        transaction.update({
            'fa2_address': asset['fa2_address'],
            'token_id': asset['fa2_batch'][0]['token_id'],
            'fa2_batch_amount': asset['fa2_batch'][0]['amount'],
            'end_time': transaction['parameter_value']['end_time'],
            'min_raise': transaction['parameter_value']['min_raise'],
            'round_time': transaction['parameter_value']['round_time'],
            'start_time': transaction['parameter_value']['start_time'],
            'extend_time': transaction['parameter_value']['extend_time'],
            'opening_price': transaction['parameter_value']['opening_price'],
            'min_raise_percent': transaction['parameter_value']['min_raise_percent'],
            'add_operator': None,
            'min_out': None,
            'receiver': None
        })
    else:
        parameter_value = transaction['parameter_value']
        if isinstance(parameter_value, list):
            add_operator = parameter_value[0].get('add_operator')
            if add_operator:
                transaction.update({
                    'owner': add_operator.get('owner'),
                    'operator': add_operator.get('operator'),
                    'token_id': add_operator.get('token_id')
                })
            else:
                transaction.update({
                    'owner': None,
                    'operator': None,
                    'token_id': None
                })
        else:
            transaction.update({
                'owner': None,
                'operator': None,
                'token_id': None
            })
            if isinstance(parameter_value, dict):  # check if parameter_value is a dictionary
                transaction.update({
                    'min_out': parameter_value.get('min_out'),
                    'receiver': parameter_value.get('receiver'),
                    'add_operator': None
                })
            else:
                transaction.update({
                    'min_out': None,
                    'receiver': None,
                    'add_operator': None
                })

    transactions.append(transaction)

print(transactions)
