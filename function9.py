def person_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}:{value}")
person_details(name="pinky",age=21,city="ahmedabad")