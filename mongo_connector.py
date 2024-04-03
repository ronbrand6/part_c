from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
# mongodb+srv://ronbrand6:<password>@cluster0.qak4lbq.mongodb.net/
uri = "mongodb+srv://ronbrand6:qQrqq8gtSMedZ2ex@cluster0.qak4lbq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    # client.admin.command('ping')
    # print("Pinged your deployment. You successfully connected to MongoDB!")
    mydb = client["group_33"]
    user_col = mydb["user"]
    contact_us_col = mydb["contact_us"]
    meeting_col = mydb["meeting"]
    # x = mycollections.insert_one(mydict)

except Exception as e:
    print(e)


