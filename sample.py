from pymongo import MongoClient

# MongoDB connection parameters
MONGO_DB_URL = "mongodb://localhost:27017"
MONGO_DATABASE = "metadata"
LINEAR_SERVICE_COLLECTION = "hsa_services"
LINEAR_PACKAGE_COLLECTION = "hsa_packages"
IDLOOKUP_COLLECTION = "station_metadata"
FORMATTED_IDLOOKUP_COLLECTION = "formatted_station_metadata"

# Connect to MongoDB
client = MongoClient(MONGO_DB_URL)
db = client[MONGO_DATABASE]

# Access the collections
service_collection = db[LINEAR_SERVICE_COLLECTION]
package_collection = db[LINEAR_PACKAGE_COLLECTION]
idlookup_collection = db[IDLOOKUP_COLLECTION]
formatted_idlookup_collection = db[FORMATTED_IDLOOKUP_COLLECTION]


# Function to retrieve and process data
def retrieve_and_process_data():
    # Retrieve data from formatted station metadata collection
    formatted_metadata = formatted_idlookup_collection.find()

    # Process each document in the formatted metadata collection
    for document in formatted_metadata:
        # Extract relevant fields from the document
        station_id = document.get("station_id")
        formatted_data = document.get("formatted_data")

        # Perform any necessary processing on the formatted data
        # For example, you might want to insert it into another collection or update existing documents
        # Here, we simply print the data as an example
        print(f"Station ID: {station_id}, Formatted Data: {formatted_data}")

        # Insert processed data into another collection or perform updates
        # Uncomment and modify the following lines as needed
        # new_document = {"station_id": station_id, "processed_data": formatted_data}
        # idlookup_collection.insert_one(new_document)


# Run the data retrieval and processing function
retrieve_and_process_data()

# Close the MongoDB connection
client.close()
