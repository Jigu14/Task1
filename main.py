from json import load
import re

with open("test.json") as json_file:
    data = load(json_file)
# print(data)s
# data = loads(data)
for key in data:
    print(type(key))
    new_key = re.sub("+test","+size@5+type",key)
    # new_key = key.replace("+test","+size@5+type")
    print(new_key)
