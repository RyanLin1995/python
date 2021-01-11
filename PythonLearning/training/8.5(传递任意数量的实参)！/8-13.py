def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key,value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('ryan', 'lin', location = 'foshan', age = '25', favorite = 'game')
print(user_profile)

for key,value in user_profile.items():
    print(key)