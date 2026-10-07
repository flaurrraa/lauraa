data = {x * 2 for x in range(5)}

print(data)

data_frozen = frozenset(data)
print(data_frozen)