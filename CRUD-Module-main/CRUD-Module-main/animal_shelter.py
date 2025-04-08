from pymongo import MongoClient
from typing import Dict, List, Union

class animalShelter(object):
    def __init__(self, username, password, host, database_name, collection_name, port ):
        self.username = 'aacuser'
        self.password = 'SNHU1234'
        self.host = '127.0.0.1'
        self.port = 8050
        self.database_name = 'aac'
        self.collection_name = 'animals'

    def _connect(self):
        uri = f"mongodb://{self.username}:{self.password}@{self.host}:{self.port}/?directConnection=true&appName=mongosh+2.4.2"
        self.client = MongoClient()
        self.database = self.client[self.database_name]
        self.collection = self.database[self.collection_name]

    def create(self, data: Union[Dict, List[Dict]]) -> bool:
        if data is not None:
            if isinstance(data, list):
                result = self.collection.insert_many(data)
                inserted_count = len(result.inserted_ids)
                print(f"Successfully inserted {inserted_count} documents.")
                return True
            elif isinstance(data, dict):
                result = self.collection.insert_one(data)
                if result.inserted_id:
                    print("Successfully inserted one document.")
                    return True
                else:
                    print("Failed to insert document.")
                    return False
            else:
                raise TypeError("Data must be a dictionary or a list of dictionaries.")
                return False  # Unreachable
        else:
            raise ValueError("Data parameter cannot be None.")
            return False  # Unreachable

    def read(self, query: Dict) -> List[Dict]:
        results: List[Dict] = list(self.collection.find(query))
        if results:
            print("Results:", results)
            return results
        else:
            print("No documents found matching the query.")
            return []

    def update(self, query: Dict, update_data: Dict) -> int:
        if not query:
            raise ValueError("Update query cannot be empty.")
        if not update_data:
            raise ValueError("Update data cannot be empty.")

        update_result = self.collection.update_many(query, {'$set': update_data})
        modified_count = update_result.modified_count
        print(f"Successfully updated {modified_count} documents matching the query.")
        return modified_count

    def delete(self, query: Dict) -> int:
        if not query:
            raise ValueError("Delete query cannot be empty.")

        delete_result = self.collection.delete_many(query)
        deleted_count = delete_result.deleted_count
        print(f"Successfully deleted {deleted_count} documents matching the query: {query}")
        return deleted_count

if __name__ == "__main__":
    shelter = animalShelter('username', 'password', 'host', 'database', 'collection', 'port')

