class Gender:
    male = 'male'
    female = 'female'


class Person:
    def __init__(self, first_name, middle_name, last_name, birthday, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = birthday
        self.gender = gender
        self.number = hash(frozenset([first_name, last_name, middle_name, birthday, gender]))
        if self.number < 0:
            self.number *= -1

    def where(self, alias):
        return f'{alias}.Name = "{self.first_name}" AND {alias}.FamalyName = "{self.last_name}" AND {alias}.DateOfBirth = date("{self.birthday}") AND {alias}.Gender = "{self.gender}"'


class City:
    def __init__(self, name):
        self.name = name
        self.number = hash(frozenset([name]))
        if self.number < 0:
            self.number *= -1

    def where(self, alias):
        return f'{alias}.Name = "{self.name}"'


class Pattern:
    @staticmethod
    def person(person: Person):
        return 'CREATE (u{}:Person '.format(person.number) + '{' + 'Name: "{}", FamalyName: "{}", DateOfBirth: date("{}"), Gender: "{}"'.format(person.first_name, person.last_name, person.birthday, person.gender) + '})'

    @staticmethod
    def city(city: City):
        return 'CREATE (c{}:City '.format(city.number) + '{' + 'Name: "{}"'.format(city.name) + '})'

    @staticmethod
    def child_of(child: Person, parent: Person):
        return f'''
            CREATE (u{child.number})-[:Child_of]->(u{parent.number}),
              (u{parent.number})-[:Parent_of]->(u{child.number})
        '''

    @classmethod
    def parent_of(cls, parent: Person, child: Person):
        return cls.child_of(child, parent)

    @staticmethod
    def is_spouse(first: Person, second: Person):
        return f'''
            CREATE (u{first.number})-[:Is_spouse]->(u{second.number}),
              (u{second.number})-[:Is_spouse]->(u{first.number})
        '''

    @staticmethod
    def live_in(person: Person, city: City):
        return f'''
            CREATE (u{person.number})-[:Live_in]->(c{city.number})
        '''


tyumen = City('Питер')
moscow = City('Москва')
print(Pattern.city(city=moscow))

# Мама папа я
print(Pattern.city(city=tyumen))
me = Person('Артем', 'Андреевич', 'Комаров', '2000-06-19', Gender.male)
print(Pattern.person(person=me))
print(Pattern.live_in(person=me, city=tyumen))
mom = Person('Анастасия', 'Александровна', 'Шикроких', '1974-05-13', Gender.female)
print(Pattern.person(person=mom))
print(Pattern.child_of(me, mom))
print(Pattern.live_in(person=mom, city=tyumen))
dad = Person('Андрей', 'Николаевич', 'Шикроких', '1971-04-12', Gender.male)
print(Pattern.person(person=dad))
print(Pattern.child_of(me, dad))
print(Pattern.is_spouse(mom, dad))
print(Pattern.live_in(person=dad, city=tyumen))

# Бабушки дедушки
# Для отца
gm1 = Person('Ирина', 'Николаевна', 'Комаров', '1955-05-19', Gender.female)
print(Pattern.person(person=gm1))
print(Pattern.child_of(dad, gm1))
print(Pattern.live_in(person=gm1, city=tyumen))
gp1 = Person('Николай', 'Геннадьевич', 'Комаров', '1955-05-19', Gender.male)
print(Pattern.person(person=gp1))
print(Pattern.child_of(dad, gp1))
print(Pattern.live_in(person=gp1, city=tyumen))
print(Pattern.is_spouse(gm1, gp1))

# Для брата отца отца
gp1_b = Person('Сергей', 'Геннадьевич', 'Комаров', '1956-05-19', Gender.male)
print(Pattern.person(person=gp1_b))
print(Pattern.live_in(person=gp1_b, city=moscow))

# Для отца отца
gp1_gm1 = Person('Кристина', 'Олеговна', 'Комаров', '1924-05-19', Gender.female)
print(Pattern.person(person=gp1_gm1))
print(Pattern.child_of(gp1, gp1_gm1))
print(Pattern.child_of(gp1_b, gp1_gm1))
print(Pattern.live_in(person=gp1_gm1, city=moscow))
gp1_gp1 = Person('Геннадий', 'Дмитриевич', 'Комаров', '1922-05-19', Gender.male)
print(Pattern.person(person=gp1_gp1))
print(Pattern.child_of(gp1, gp1_gp1))
print(Pattern.child_of(gp1_b, gp1_gp1))
print(Pattern.live_in(person=gp1_gp1, city=moscow))
print(Pattern.is_spouse(gp1_gm1, gp1_gp1))

# Семья двоюродного брата

sb = Person('Никита', 'Антонович', 'Кузнецов', '2004-07-19', Gender.male)
print(Pattern.person(person=sb))
print(Pattern.live_in(person=sb, city=moscow))
sb_mom = Person('Юлия', 'Сергеевна', 'Кузнецова', '1974-05-13', Gender.female)
print(Pattern.person(person=sb_mom))
print(Pattern.child_of(sb, sb_mom))
print(Pattern.live_in(person=sb_mom, city=moscow))
sb_dad = Person('Антон', 'Дмитриевич', 'Кузнецов', '1971-04-12', Gender.male)
print(Pattern.person(person=sb_dad))
print(Pattern.child_of(sb, sb_dad))
print(Pattern.is_spouse(sb_mom, sb_dad))
print(Pattern.live_in(person=sb_dad, city=moscow))

# Для матери
gm2 = Person('Ольга', 'Аркадьевна', 'Кузнецова', '1955-05-19', Gender.female)
print(Pattern.person(person=gm2))
print(Pattern.child_of(mom, gm2))
print(Pattern.child_of(sb_dad, gm2))
print(Pattern.live_in(person=gm2, city=moscow))
gp2 = Person('Александр', 'Васильевич', 'Кузнецов', '1955-05-19', Gender.male)
print(Pattern.person(person=gp2))
print(Pattern.child_of(mom, gp2))
print(Pattern.child_of(sb_dad, gp2))
print(Pattern.live_in(person=gp2, city=moscow))
print(Pattern.is_spouse(gm2, gp2))
