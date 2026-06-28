class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    new_list = []
    for pe in people:
        new_list.append(Person(pe["name"], pe["age"]))
    for pe in people:
        person = Person.people[pe["name"]]
        if pe["wife"] is not None:
            person.wife = Person.people[pe["wife"]]
        if pe["husband"] is not None:
            person.husband = Person.people[pe["husband"]]
    return new_list
