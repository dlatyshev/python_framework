import json


data = """{
    "key1": 1,
    "key2": 2,
    "key3": [1, 2, 3]
}"""

parsed_data = json.loads(data)
print(parsed_data)

print(parsed_data['key1'])
print(parsed_data['key2'])
print(parsed_data['key3'])


data_dict = {"key1": 1, "key2": 2, "key3": [1, 2, 3]}
parsed_to_string_data = json.dumps(data_dict)

print(parsed_to_string_data)
