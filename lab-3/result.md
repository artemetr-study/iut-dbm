# Широких Артем. АСОиУб-18-1. ЛР3

1. Создать пустой sandbox на sandbox.neo4j.com
2. Создать генеалогическое дерево своих родственников, включая себя:
    * Тип узла: Person
        * Атрибуты узлов: Name, FamalyName, DateOfBirth, Gender
    * Тип узла: City
        * Атрибуты узлов: Name
    * Связи: Child_of, Parent_of, Is_spouse (является ребенком, является родителем, является
супругом), Live_in (живет в)
```neo4j
CREATE (c3937750479132411881:City {Name: "Москва"})
CREATE (c780096638066174912:City {Name: "Тюмень"})
CREATE (u6603581725950569980:Person {Name: "Артем", FamalyName: "Широких", DateOfBirth: date("2000-06-19"), Gender: "male"})

CREATE (u6603581725950569980)-[:Live_in]->(c780096638066174912)
        
CREATE (u3079738898284056088:Person {Name: "Анастасия", FamalyName: "Шикроких", DateOfBirth: date("1974-05-13"), Gender: "female"})

CREATE (u6603581725950569980)-[:Child_of]->(u3079738898284056088),
  (u3079738898284056088)-[:Parent_of]->(u6603581725950569980)

CREATE (u3079738898284056088)-[:Live_in]->(c780096638066174912)
        
CREATE (u4199280607187406316:Person {Name: "Андрей", FamalyName: "Шикроких", DateOfBirth: date("1971-04-12"), Gender: "male"})

CREATE (u6603581725950569980)-[:Child_of]->(u4199280607187406316),
  (u4199280607187406316)-[:Parent_of]->(u6603581725950569980)

CREATE (u3079738898284056088)-[:Is_spouse]->(u4199280607187406316),
  (u4199280607187406316)-[:Is_spouse]->(u3079738898284056088)

CREATE (u4199280607187406316)-[:Live_in]->(c780096638066174912)
        
CREATE (u5815547902927381573:Person {Name: "Ирина", FamalyName: "Широких", DateOfBirth: date("1955-05-19"), Gender: "female"})

CREATE (u4199280607187406316)-[:Child_of]->(u5815547902927381573),
  (u5815547902927381573)-[:Parent_of]->(u4199280607187406316)

CREATE (u5815547902927381573)-[:Live_in]->(c780096638066174912)
        
CREATE (u8765517599201879674:Person {Name: "Николай", FamalyName: "Широких", DateOfBirth: date("1955-05-19"), Gender: "male"})

CREATE (u4199280607187406316)-[:Child_of]->(u8765517599201879674),
  (u8765517599201879674)-[:Parent_of]->(u4199280607187406316)

CREATE (u8765517599201879674)-[:Live_in]->(c780096638066174912)

CREATE (u5815547902927381573)-[:Is_spouse]->(u8765517599201879674),
  (u8765517599201879674)-[:Is_spouse]->(u5815547902927381573)
        
CREATE (u4408781529534511445:Person {Name: "Сергей", FamalyName: "Широких", DateOfBirth: date("1956-05-19"), Gender: "male"})

CREATE (u4408781529534511445)-[:Live_in]->(c3937750479132411881)
        
CREATE (u7529370526513518723:Person {Name: "Кристина", FamalyName: "Широких", DateOfBirth: date("1924-05-19"), Gender: "female"})

CREATE (u8765517599201879674)-[:Child_of]->(u7529370526513518723),
  (u7529370526513518723)-[:Parent_of]->(u8765517599201879674)

CREATE (u4408781529534511445)-[:Child_of]->(u7529370526513518723),
  (u7529370526513518723)-[:Parent_of]->(u4408781529534511445)

CREATE (u7529370526513518723)-[:Live_in]->(c3937750479132411881)
        
CREATE (u7250441663953576738:Person {Name: "Геннадий", FamalyName: "Широких", DateOfBirth: date("1922-05-19"), Gender: "male"})

CREATE (u8765517599201879674)-[:Child_of]->(u7250441663953576738),
  (u7250441663953576738)-[:Parent_of]->(u8765517599201879674)

CREATE (u4408781529534511445)-[:Child_of]->(u7250441663953576738),
  (u7250441663953576738)-[:Parent_of]->(u4408781529534511445)

CREATE (u7250441663953576738)-[:Live_in]->(c3937750479132411881)

CREATE (u7529370526513518723)-[:Is_spouse]->(u7250441663953576738),
  (u7250441663953576738)-[:Is_spouse]->(u7529370526513518723)
        
CREATE (u8753977556437968371:Person {Name: "Никита", FamalyName: "Кузнецов", DateOfBirth: date("2004-07-19"), Gender: "male"})

CREATE (u8753977556437968371)-[:Live_in]->(c3937750479132411881)
        
CREATE (u7230800693964760372:Person {Name: "Юлия", FamalyName: "Кузнецова", DateOfBirth: date("1974-05-13"), Gender: "female"})

CREATE (u8753977556437968371)-[:Child_of]->(u7230800693964760372),
  (u7230800693964760372)-[:Parent_of]->(u8753977556437968371)

CREATE (u7230800693964760372)-[:Live_in]->(c3937750479132411881)
        
CREATE (u4855619786865060708:Person {Name: "Антон", FamalyName: "Кузнецов", DateOfBirth: date("1971-04-12"), Gender: "male"})

CREATE (u8753977556437968371)-[:Child_of]->(u4855619786865060708),
  (u4855619786865060708)-[:Parent_of]->(u8753977556437968371)

CREATE (u7230800693964760372)-[:Is_spouse]->(u4855619786865060708),
  (u4855619786865060708)-[:Is_spouse]->(u7230800693964760372)

CREATE (u4855619786865060708)-[:Live_in]->(c3937750479132411881)
        
CREATE (u5319806461678995424:Person {Name: "Ольга", FamalyName: "Кузнецова", DateOfBirth: date("1955-05-19"), Gender: "female"})

CREATE (u3079738898284056088)-[:Child_of]->(u5319806461678995424),
  (u5319806461678995424)-[:Parent_of]->(u3079738898284056088)

CREATE (u4855619786865060708)-[:Child_of]->(u5319806461678995424),
  (u5319806461678995424)-[:Parent_of]->(u4855619786865060708)

CREATE (u5319806461678995424)-[:Live_in]->(c3937750479132411881)
        
CREATE (u2827531146440745354:Person {Name: "Александр", FamalyName: "Кузнецов", DateOfBirth: date("1955-05-19"), Gender: "male"})

CREATE (u3079738898284056088)-[:Child_of]->(u2827531146440745354),
  (u2827531146440745354)-[:Parent_of]->(u3079738898284056088)

CREATE (u4855619786865060708)-[:Child_of]->(u2827531146440745354),
  (u2827531146440745354)-[:Parent_of]->(u4855619786865060708)

CREATE (u2827531146440745354)-[:Live_in]->(c3937750479132411881)

CREATE (u5319806461678995424)-[:Is_spouse]->(u2827531146440745354),
  (u2827531146440745354)-[:Is_spouse]->(u5319806461678995424)
```
3. Выбрать всех Александров у которых есть дочь.
```neo4j
MATCH (:Person {Gender: 'female'})-[Child_of]->(a:Person {Name: 'Александр'}) RETURN DISTINCT a.Name, a.FamalyName, a.DateOfBirth, a.Gender
```
```json
[
  {
    "a.Name": "Александр",
    "a.FamalyName": "Кузнецов",
    "a.DateOfBirth": "1955-05-19",
    "a.Gender": "male"
  }
]
```
4. Выбрать всех своих бабушек
```neo4j
MATCH (:Person {Name: 'Артем', FamalyName: 'Широких'})-[:Child_of]->(:Person)-[:Child_of]->(target:Person {Gender: 'female'}) RETURN target.Name, target.FamalyName, target.DateOfBirth
```
```json
[
  {
    "target.Name": "Ирина",
    "target.FamalyName": "Широких",
    "target.DateOfBirth": "1955-05-19"
  },
  {
    "target.Name": "Ольга",
    "target.FamalyName": "Кузнецова",
    "target.DateOfBirth": "1955-05-19"
  }
]
```
5. Выбрать всех своих прадедушек, у которых есть 2 сына
```neo4j
MATCH (:Person {Name: 'Артем', FamalyName: 'Широких'})-[:Child_of]->(:Person)-[:Child_of]->(:Person)-[:Child_of]->(target:Person {Gender: 'male'}) WHERE size((target)-[:Parent_of]->(:Person {Gender: 'male'})) = 2 RETURN target.Name, target.FamalyName, target.DateOfBirth
```
```json
[
  {
    "target.Name": "Геннадий",
    "target.FamalyName": "Широких",
    "target.DateOfBirth": "1922-05-19"
  }
]
```
6. Всех супругов, у которых есть 2 ребенка
```neo4j
MATCH (mom:Person {Gender: 'female'})<-[:Is_spouse]->(dad:Person {Gender: 'male'}) WHERE size((mom)-[:Parent_of]->(:Person)-[:Child_of]->(dad)) = 2 RETURN DISTINCT mom.Name, mom.FamalyName, dad.Name, dad.FamalyName
```
```json
[
  {
    "mom.Name": "Кристина",
    "mom.FamalyName": "Широких",
    "dad.Name": "Геннадий",
    "dad.FamalyName": "Широких"
  },
  {
    "mom.Name": "Ольга",
    "mom.FamalyName": "Кузнецова",
    "dad.Name": "Александр",
    "dad.FamalyName": "Кузнецов"
  }
]
```
7. Выбрать всех родственников, родившихся после 2000г.
```neo4j
MATCH (target:Person) WHERE target.DateOfBirth >= date("2001") RETURN DISTINCT target.Name, target.FamalyName, target.DateOfBirth
```
```json
[
  {
    "target.Name": "Никита",
    "target.FamalyName": "Кузнецов",
    "target.DateOfBirth": "2004-07-19"
  }
]
```
8. Выбрать всех родственников живущих или живших в городе Тюмень.
```neo4j
MATCH (:City {Name: "Тюмень"})<-[:Live_in]-(target:Person) RETURN DISTINCT target.Name, target.FamalyName, target.DateOfBirth
```
```json
[
  {
    "target.Name": "Николай",
    "target.FamalyName": "Широких",
    "target.DateOfBirth": "1955-05-19"
  },
  {
    "target.Name": "Ирина",
    "target.FamalyName": "Широких",
    "target.DateOfBirth": "1955-05-19"
  },
  {
    "target.Name": "Андрей",
    "target.FamalyName": "Шикроких",
    "target.DateOfBirth": "1971-04-12"
  },
  {
    "target.Name": "Анастасия",
    "target.FamalyName": "Шикроких",
    "target.DateOfBirth": "1974-05-13"
  },
  {
    "target.Name": "Артем",
    "target.FamalyName": "Широких",
    "target.DateOfBirth": "2000-06-19"
  }
]
```
9. Вывести названия городов, которых живут двоюродные братья.
```neo4j
MATCH (c1:City)<-[:Live_in]-(b1:Person {Gender: "male"})-[:Child_of]->(:Person)-[:Child_of]->(:Person)-[:Parent_of]->(:Person)-[:Parent_of]->(b2:Person {Gender: "male"})-[:Live_in]->(c2:City) RETURN DISTINCT c1.Name, b1.Name, c2.Name, b2.Name
```
```json
[
  {
    "c1.Name": "Москва",
    "b1.Name": "Никита",
    "c2.Name": "Тюмень",
    "b2.Name": "Артем"
  },
  {
    "c1.Name": "Тюмень",
    "b1.Name": "Артем",
    "c2.Name": "Москва",
    "b2.Name": "Никита"
  }
]
```
