import json

# load the data
with open('trainingSet1Cleaned.json', 'r') as f:
    json_data = json.load(f)


levels = []
sender_addresses = []
sender_aliases = []
target_addresses = []
target_aliases = []
amounts = []
parameter_entrypoints = []
parameter_min_outs = []
parameter_receivers = []
fa2_addresses = []
token_ids = []
fa2_batch_amounts = []
end_times = []
min_raises = []
round_times = []
start_times = []
extend_times = []
opening_prices = []
min_raise_percents = []
owners = []
operators = []

# iterate through transactions in the data file
for item in json_data:
    level = item['level']
    sender_address = item['sender'].get('address')
    sender_alias = item['sender'].get('alias')
    target_address = item['target'].get('address')
    target_alias = item['target'].get('alias')
    amount = item['amount']
    parameter_entrypoint = item.get('parameter', {}).get('entrypoint')
    parameter_value = item.get('parameter', {}).get('value')
    
    # extract additional fields if the transaction is of type "configure"
    if parameter_entrypoint == 'configure':
        asset = parameter_value['asset'][0]
        fa2_address = asset['fa2_address']
        fa2_batch = asset['fa2_batch'][0]
        token_id = fa2_batch['token_id']
        fa2_batch_amount = fa2_batch['amount']
        end_time = parameter_value['end_time']
        min_raise = parameter_value['min_raise']
        round_time = parameter_value['round_time']
        start_time = parameter_value['start_time']
        extend_time = parameter_value['extend_time']
        opening_price = parameter_value['opening_price']
        min_raise_percent = parameter_value['min_raise_percent']
        
        # append additional extracted values to respective lists
        fa2_addresses.append(fa2_address)
        token_ids.append(token_id)
        fa2_batch_amounts.append(fa2_batch_amount)
        end_times.append(end_time)
        min_raises.append(min_raise)
        round_times.append(round_time)
        start_times.append(start_time)
        extend_times.append(extend_time)
        opening_prices.append(opening_price)
        min_raise_percents.append(min_raise_percent)
        
        # set default values for keys that may be missing
        add_operator = None
        min_out = None
        receiver = None
    else:
        # extract values from the parameter dictionary
        if isinstance(parameter_value, dict):
            add_operator = parameter_value.get('add_operator')
            if add_operator:
                owner = add_operator.get('owner')
                operator = add_operator.get('operator')
                token_id = add_operator.get('token_id')
            else:
                owner = None
                operator = None
                token_id = None

            min_out = parameter_value.get('min_out')
            receiver = parameter_value.get('receiver')
        else:
            add_operator = None
            min_out = None
            receiver = None
            
        # set default values for keys that may be missing
        fa2_address = None
        fa2_batch_amount = None
        end_time = None
        min_raise = None
        round_time = None
        start_time = None
        extend_time = None
        opening_price = None
        min_raise_percent = None
        
    # append extracted values to respective lists
    levels.append(level)
    sender_addresses.append(sender_address)
    sender_aliases.append(sender_alias)
    target_addresses.append(target_address)
    target_aliases.append(target_alias)
    amounts.append(amount)
    parameter_entrypoints.append(parameter_entrypoint)
    parameter_min_outs.append(min_out)
    parameter_receivers.append(receiver)
    fa2_addresses.append(fa2_address)

    
print("Levels:", levels)
print("Sender addresses:", sender_addresses)
print("Sender aliases:", sender_aliases)
print("Target addresses:", target_addresses)
print("Target aliases:", target_aliases)
print("Amounts:", amounts)
print("Parameter entrypoints:", parameter_entrypoints)
print("Parameter min_outs:", parameter_min_outs)
print("Parameter receivers:", parameter_receivers)
print("FA2 addresses:", fa2_addresses)
print("Token IDs:", token_ids)
print("FA2 batch amounts:", fa2_batch_amounts)
print("End times:", end_times)
print("Min raises:", min_raises)
print("Round times:", round_times)
print("Start times:", start_times)
print("Extend times:", extend_times)
print("Opening prices:", opening_prices)
print("Min raise percents:", min_raise_percents)