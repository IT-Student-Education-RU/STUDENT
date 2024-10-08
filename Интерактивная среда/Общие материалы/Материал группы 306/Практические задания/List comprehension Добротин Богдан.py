data = {'key1': 'value1', 'key2': 'value2', 'long_key': 'value3', 'short': 'value4'}
filtered_keys = [key for key in data if len(key) > 3]
print(filtered_keys)
filtered_keys = list(filter(lambda key: len(key) > 3, data))
print(filtered_keys)


input()
