def get_full_name(first_name, last_name=""):
    return f"{first_name} {last_name}".strip()

print(get_full_name("Darion"))
print(get_full_name("Darion", "Mograine"))