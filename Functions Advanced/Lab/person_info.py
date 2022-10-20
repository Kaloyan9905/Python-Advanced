def get_info(**kwargs):
    for key, value in kwargs.items():
        return f"This is {kwargs.get('name')} from {kwargs.get('town')} " \
               f"and he is {kwargs.get('age')} years old"


print(get_info(**{"name": "George", "town": "Sofia", "age": 20}))
