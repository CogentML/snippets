import json

# Define the configuration dictionary
config = {
    'client_id': 'abcd',
    'client_secret': 'abcd',
    'username': 'abc@xyz.com',
    'password': '******',
}

# Write the configuration dictionary to a JSON file
with open('config.json', 'w') as f:
    json.dump(config, f)