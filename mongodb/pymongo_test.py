from pymongo_test_insert import get_database
from dateutil import parser

dbname = get_database()
collection_name = dbname["user_1_items"]



expiry_date = '2021-08-13T00:00:00.000Z'
expiry = parser.parse(expiry_date)
item_3 = {
"item_name" : "Medias Noches",
"quantity" : 2,
"ingredients" : "all-purpose flour",
"expiry_date" : expiry
}
collection_name.insert_one(item_3)
