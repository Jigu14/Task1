from json import loads
import re

with open("test.json") as json_file:
    data = loads(json_file.read())

output_data = {}
for key,values in data.items():
    new_key = key.replace("+type","+size@5+type")
    output_data[str(new_key)] = {}
    for val in values:
        item = data[key][val]
        if type(item) == str:
            new_value = item.replace("+type","+size@5+type")
            output_data[new_key][val] = new_value
            # print(new_value)
        else:
            new_value_list = []
            for x in item:
                new_value = x.replace("+type","+size@5+type")
                new_value_list.append(new_value)
                # print(new_value)
            output_data[new_key][val] = new_value_list

print(output_data)