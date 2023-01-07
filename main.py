users = [
    {"name": "a", "age": "35"},
    {"name": "b", "age": "32"},
    {"name": "c", "age": "22"},
    {"name": "d", "age": "77"},
    {"name": "e", "age": "19"},
    {"name": "f", "age": "18"}
]

users_age = []  # empty list

for user in users:  # get every "age" values and append them into users_age list
    users_age.append(user["age"])

users_age.sort()    # sort values

users_age_int = [eval(i) for i in users_age]    # convert values to numbers

print(users_age)
print(users_age_int)