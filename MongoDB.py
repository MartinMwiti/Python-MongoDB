from pymongo import MongoClient

#Making a Connection with MongoClient
#client = MongoClient() #code will connect on the default host and port
client = MongoClient('localhost', 27017) #specify the host and port explicitly
#client = MongoClient('mongodb://localhost:27017/')

mydb = client['mydatabase'] #database name
mycol = mydb['customers'] #database collection name

#insert a record in the 'customers' collection
mydict = {'name':'John', 'address': 'Highway 37'}

x = mycol.insert_one(mydict)
print(x.inserted_id)  #'inserted_id' holds the id of the inserted document. If you don't specify id field, MongoDB will add one

#check if collection exists
print(mydb.list_collection_names())
collist=mydb.list_collection_names()
if 'customers' in collist:
    print('The collection exists.')

#check name of existing database
#print(mydb.list_database_names)

#Insert Multiple Documents
mylist =[
    {'name': 'Amy', 'address': 'Apple st 652'},
    {'name':'Hannah', 'address': 'Mountain 21'},
    {'name': 'Michael', 'address': 'Valley 345'},
    {'name':'Sandy', 'address': 'Ocean blvd 2'},
    {'name': 'Betty', 'address': 'Sky at 331'},
    {'name': 'Richard', 'address':'One Way 98'},
    {'name': 'Susan', 'address':'Yellow Garden 2'}
]

x = mycol.insert_many(mylist)
print(x.inserted_ids)

#Insert Multiple Documents, with Specified IDs

mylist = [
    {'_id': 1, 'name': 'Amy', 'address': 'Apple st 652'},
    {'_id': 2, 'name': 'Hannah', 'address': 'Mountain 21'},
    {'_id': 3, 'name': 'Michael', 'address': 'Valley 345'},
    {'_id': 4, 'name': 'Sandy', 'address': 'Ocean blvd 2'},
    {'_id': 5, 'name': 'Betty', 'address': 'Sky at 331'},
    {'_id': 6, 'name': 'Richard', 'address': 'One Way 98'},
    {'_id': 7, 'name': 'Susan', 'address': 'Yellow Garden 2'}
]

x = mycol.insert_many(mylist)
print(x.inserted_ids)

