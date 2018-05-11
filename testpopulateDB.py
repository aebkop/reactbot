from tinydb import TinyDB, Query
db = TinyDB('database.json')
db.purge()
