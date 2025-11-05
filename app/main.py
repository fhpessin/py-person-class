class Person:
    """
    Representa uma pessoa com nome e idade, e gerencia um registro global
    de todas as instâncias criadas.
    """
    # 1. Definir o atributo de classe para armazenar todas as instâncias.
    people = {}

    def __init__(self, name: str, age: int):
        # 2. Inicializar atributos de instância
        self.name = name
        self.age = age

        # 3. Adicionar a nova instância ao dicionário de classe 'people'.
        Person.people[self.name] = self

# --- FIM DA CLASSE PERSON ---

def create_person_list(people_data: list) -> list:
    """
    Cria instâncias da classe Person a partir de uma lista de dicionários
    e estabelece as relações de casamento.

    Args:
        people_data: Uma lista de dicionários com dados das pessoas.

    Returns:
        Uma lista contendo as instâncias da classe Person.
    """
    # 1. Primeira Etapa: Criar todas as instâncias e popular Person.people
    # Esta etapa garante que todas as pessoas existam antes de tentarmos
    # criar os links de casamento.
    person_instances = []
    for data in people_data:
        # Apenas os dados essenciais (name e age) são passados para o __init__
        person = Person(name=data["name"], age=data["age"])
        person_instances.append(person)

    # 2. Segunda Etapa: Estabelecer os links de casamento
    # Iteramos sobre a lista de dicionários original (people_data)
    # E usamos Person.people para encontrar a instância correta.
    for data in people_data:
        # Recupera a instância Person recém-criada usando o nome.
        current_person = Person.people[data["name"]]

        # Verifica se há um cônjuge (wife ou husband) no dicionário.
        # Usa .get() para lidar com dicionários que podem não ter a chave.
        spouse_name = data.get("wife") or data.get("husband")
        
        if spouse_name is not None:
            # 3. Encontra a instância do cônjuge no registro global 'people'.
            spouse_instance = Person.people.get(spouse_name)

            if spouse_instance:
                # 4. Adiciona o atributo wife/husband ao objeto Person.
                if "wife" in data:
                    current_person.wife = spouse_instance
                elif "husband" in data:
                    current_person.husband = spouse_instance
            # Nota: Não precisamos de um 'else' se o nome do cônjuge não for encontrado,
            # pois o requisito implica que ele sempre existirá.

    return person_instances
