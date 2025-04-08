## Emergency Animal Shelter Outcomes
![image](https://github.com/user-attachments/assets/daa53517-35dc-4138-834a-cc66f49a0d2a)
<img width="1680" alt="Screenshot 2025-04-08 at 12 54 49 PM (2)" src="https://github.com/user-attachments/assets/98253f05-3fad-49ff-ba9a-105dcbe2e419" />



## Tools Used:
    VS Code Python, Jupyter Notebooks exstension in VS Code, Prettier, .venv, Flask, Jupyter, Home brew, pip (via Mac OS CLI), and Plotly Dash. The remaining imports and/or libraries can be found within the code base.

## Create:
    self.collection.insert_many(data) - Inserts more than one document.
    
    self.collection.insert_one(data) - Inserts a signle document.
    
    total = self.collection.count_documents({}) - Counts the total documents within the database.
    
    results = list(self.collection.find(query)) - Quick look up for existing documents.
    
## Read -
    results = list(self.collection.find(query)) - Read the preexisting documents.

## Update:
    updateOne = list(self.collection.updateOne()) - Updates a single document.
    
    updateMany = list(self.collection.updateMany()) - Updates multiple documents.
    
    replaceOne = list(self.collection.replaceOne()) - Replaces a single documents.
    
    replaceOne = list(self.collection.replaceMany()) - Replaces multiple documents. 
    
    queryCount = query - Counts how many queries are within the database curently.

## Delete:
    deleteOne = list(self.collection.deleteOne()) - Deletes a single document.
    
    deleteMany = list(seld.collection.deleteMany()) - Deletes multiple documents.
    
## Example Usage:
    Insert a document - shelter.create({"name": "Buddy", "type": "Dog", "age": 3}).
    
    Insert multiple documents - shelter.create([{"name": "Whiskers", "type": "Cat", "age": 5},{"name": "Polly", "type": "Bird", "age": 1}]).
    
    Read all dogs - dogs = shelter.read({"type": "Dog"}).
    print("Dogs:", dogs).

    Update Buddy's age - updated_count = shelter.update({"name": "Buddy"}, {"age": 4}).
    print("Updated count:", updated_count).

    Delete Polly - deleted_count = shelter.delete({"name": "Polly"}).
    print("Deleted count:", deleted_count).
    


