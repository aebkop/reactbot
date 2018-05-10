from tinydb import TinyDB, Query
db = TinyDB('db.json')
db.insert({'key': 'microsoft', 'message': 'fwefwefe'})
db.insert({'key': 'linux', 'message': 'eger'})

