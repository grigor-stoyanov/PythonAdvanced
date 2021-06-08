def age_assignment(*args, **kwargs):
    age_dict = {}
    for name in args:
        age_dict[name] = kwargs.get(name[0])
    return age_dict


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
