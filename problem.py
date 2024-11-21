dict1 = { "a": { "b": { "c": 1 }, "d": 2 }, "e": 3 }

key = []
val = []


for key,val in dict1.items():
    if isinstance(val, dict):
        for key,val in val.items():
            if isinstance(val, dict):
                for key,val in val.items():
                    print(key, val)
    else:
        print(key, val)


