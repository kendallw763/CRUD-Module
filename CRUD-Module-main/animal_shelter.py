
from traitlets import Instance
from pymongo import MongoClientClass AnimalShelter(object): # type: ignore
    
def __init__(self):
      username = 'aacuser'
      password = 'SNHU1234'
      host = 'nv-desktop-services.apporto.com'
      port = 31580
      database = 'aac'
      collection = 'animals'
    
      # Initialize Connection
      self.client = MongoClient('mongodb://%s:%s@%s:%d' % (username, password, host, port, database, collection)) # type: ignore
      self.database = self.client[database]
      self.collection = self.database[collection]      
              
def create(self, data):
    if data is not None and Instance(data, list):
    
       if self.collection.insert_many(data) or self.collection.insert_one(data):
            
        total = self.collection.count_documents({})
                
        print("Successful insertion of" + str(total) +  "documents created... ")
        return True  
                      
    else:
        raise Exception("Nothing to save because data parameter is empty")
        return False  
        
def read(self, query):
    results = list(self.collection.find(query))  
    if results:
        print("Results:"  + str(results))
        return True 

    else:
        raise Exception("Nothing to read, due to unknown error or syntax issue")
        return False 
       
def update (self, query):
    updateOne = list(self.collection.updateOne())
    updateMany = list(self.collection.updateMany())
    replaceOne = list(self.collection.updateMany())
    queryCount = query 
                            
    if updateOne:
        print(updateOne)
            
    if updateMany:
        print(updateMany)
           
    if replaceOne:
        print(replaceOne)
        
    else: 
        raise Exception('The documents have been updated...' + updateOne + 
        'There are a total of' + 'queryCount:' + queryCount)
        return false; 
     
def delete(self, query):
    deleteOne = list(self.collection.deleteOne())
    deleteMany = list(self.collection.deleteMany())        
            
    if deleteOne:
        print('Document deleted: ' + deleteOne + query + 
        'Deleted query:' + query)
                
    if deleteMany:
        print('Documents deleted: '+ deleteMany + query)
    else: raise Exception('Error') 
           
   
 

