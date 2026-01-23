#
hash_map = {}
hash_map["name"] = "John"
hash_map["age"] = "20"

del hash_map["name"]
print(hash_map.pop("age"))

print(hash_map)

#
my_map = dict()
my_map["name"] = "Shawn"
my_map["age"] = 20

print("name" in my_map)
print(my_map.get("name"))
print(my_map.get("name", "Not Found"))

for key in my_map:
    print("Keys", key)

for val in my_map.values():
    print("Values", val)

for [key, val] in my_map.items():
    print("Key", key, "Value", val)
