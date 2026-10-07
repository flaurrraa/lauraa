profile = {
    "id": 2,
    "name": "mario",
    "is_female": False,
}

profile["age"] = 25
print(profile)

profile_copy = profile.copy()
print(profile_copy)

profile.clear()
print(profile)