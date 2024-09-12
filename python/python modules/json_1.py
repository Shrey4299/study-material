import json

# Example JSON data
x = {
    "name": "John",
    "age": 30,
    "married": True,
    "divorced": False,
    "children": ["Ann", "Billy"],  # Fixed to a list for valid JSON
    "pets": None,
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
    ]
}

# Example 1: Convert Python dictionary to JSON string with pretty print
json_string = json.dumps(x, indent=4, sort_keys=True, separators=(". ", " = "))
print("Pretty-printed JSON string with sorted keys:")
print(json_string)

# Example 2: Convert JSON string to Python dictionary
json_data = '{"name":"John", "age":30, "city":"New York"}'
parsed_data = json.loads(json_data)
print("\nParsed JSON data:")
print(parsed_data)
print("Age:", parsed_data["age"])

# Example 3: Convert Python dictionary to JSON string without pretty print
compact_json_string = json.dumps(x)
print("\nCompact JSON string:")
print(compact_json_string)

# Example 4: Write JSON data to a file
with open('data.json', 'w') as file:
    json.dump(x, file, indent=4)

print("\nJSON data has been written to 'data.json'")

# Example 5: Read JSON data from a file
with open('data.json', 'r') as file:
    file_data = json.load(file)

print("\nRead JSON data from 'data.json':")
print(file_data)

# Example 6: Handle JSON encoding and decoding with custom objects
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def person_encoder(obj):
    if isinstance(obj, Person):
        return {"name": obj.name, "age": obj.age}
    raise TypeError("Object of type Person is not JSON serializable")

person = Person("Alice", 28)
person_json = json.dumps(person, default=person_encoder, indent=4)
print("\nCustom encoded Person object:")
print(person_json)

# Example 7: Decode JSON string into a custom Python object
def person_decoder(dct):
    if "name" in dct and "age" in dct:
        return Person(dct["name"], dct["age"])
    return dct

decoded_person = json.loads(person_json, object_hook=person_decoder)
print("\nCustom decoded Person object:")
print(f"Name: {decoded_person.name}, Age: {decoded_person.age}")

# Example 8: Handle JSON serialization with complex data types
complex_data = {
    "nested_list": [1, 2, {"key": "value"}],
    "nested_dict": {"outer": {"inner": "value"}}
}
complex_json_string = json.dumps(complex_data, indent=4)
print("\nComplex JSON data:")
print(complex_json_string)
