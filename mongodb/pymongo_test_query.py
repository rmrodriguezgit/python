# Get the database using the method we defined in pymongo_test_insert file
import pandas as pd
from pymongo_test_insert import get_database
dbname = get_database()

# Create a new collection
collection_name = dbname["user_1_items"]

item_details = collection_name.find()

items_df = pd.DataFrame(item_details)
print(items_df)
