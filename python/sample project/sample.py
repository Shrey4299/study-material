import json


desc = "i am the boy in the am alive"

hmap = {}
desc_list = desc.split(" ")


for word in desc_list:
    if word not in hmap:
        hmap[word] = 1
    else:
        hmap[word] += 1

json_string = json.dumps(hmap)

print(json_string)
