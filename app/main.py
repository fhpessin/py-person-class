class Person:
    """Representa uma pessoa com nome, idade e possíveis relacionamentos."""

    people: dict[str, "Person"] = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people_data: list[dict[str, object]]) -> list[Person]:
    """Cria uma lista de instâncias Person a partir de uma lista de dicionários."""
    persons: list[Person] = []

    # 1ª passagem — cria todas as instâncias e as registra no dicionário Person.people
    for data in people_data:
        name = str(data["name"])
        age = int(data["age"])
        person = Person(name, age)
        persons.append(person)

    # 2ª passagem — cria os relacionamentos (wife/husband)
    for data in people_data:
        person = Person.people[data["name"]]

        # se tiver esposa
        if "wife" in data and data["wife"] is not None:
            wife_name = str(data["wife"])
            if wife_name in Person.people:
                person.wife = Person.people[wife_name]

        # se tiver marido
        if "husband" in data and data["husband"] is not None:
            husband_name = str(data["husband"])
            if husband_name in Person.people:
                person.husband = Person.people[husband_name]

    return persons
