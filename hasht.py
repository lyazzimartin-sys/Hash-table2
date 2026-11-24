hash_table = {}

def insert(key, value):
    hash_table[key] = value

def search(key):
    return hash_table.get(key, "Not Found")

insert("101", "Martin")
insert("102", "John")
insert("103", "Peter")

print(search("101"))
print(search("102"))
print(search("105"))
