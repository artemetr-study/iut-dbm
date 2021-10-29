cd /iut-dbm/mongodb-sakila/
mongoimport --db customers --collection customers --drop --file customers.json
mongoimport --db films --collection films --drop --file films.json
mongoimport --db stores --collection stores --drop --file stores.json
