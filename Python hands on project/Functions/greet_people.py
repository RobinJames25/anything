def build_person(first_name, last_name, middle_name,age=''):
    """Return a dictionary of information about a person."""
    person= {'first':first_name,'last':last_name,'middle':middle_name}
    if age:
        person['age'] = age
    return person
