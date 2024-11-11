## Grazioso Salvare/Global Rain.
The required functionality of this project will involve working with existing data from the animal shelter CSV file. This will give Grazioso Salvare employees the ability to identify and categorize data, specifically dog breeds. The application will also feature a client facing dashboard. Affiliates of Grazioso Salvare/Global Rain may access the database from via database queries. The users can interact with the preexisting data from the animal shelter database categorized by the rescue type of the animal (breed). The code implemented in this documentation is for CRUD operations (create, read, update, delete) functionality.  Which allows users to interact through filtering options with database collections data. 

## Tools Used
The tools used for this application were Python, Jupyter Notebooks, CLI commands, Plotly Dash, import commands used inside python files, MongoDB for the database, and a spreadsheet for dataset. MongoDB was used for this project because of its scalability along with python’s flexibility and ease of use. Of course, there are a many other reasons to choose these technologies such as pymongo’s ease of use or the number of libraries provided. Python can handle a verbose amount of data with a few lines of code. Handling large amount of data in real time is better managed through MongoDB. The scalability is what gives the program more modularity.


## Steps Taken
To begin, we will start by opening the virtual machine via Apporto. This can be accessed through Brightspace. Or, within the user's pesonal machine running Linux OS. Next, open Jupyter Notebooks. Create a new folder or use an existing folder to place the file of the prewritten code. Within the folder, we will create the ipynb file responsible for implementing and compiling our code. The source code has been made available from module four assignment information via Brightspace through Southern New Hampshire University. In some instances, the virtual machine will not allow users who use mac to copy and paste the code directly into the IDE. You may copy the code into a text file on your personal machine, upload that file into apporto through the desktop. On the upper left-hand corner of the screen on the desktop in the virtual machine, there is a button to upload files anywhere from your personal machine. Copy and paste the code into the IDE and save your work. 

## Create - This gives the user the ability to add information to the database with ease...
    self.collection.insert_many(data) - inserts more than one document
    self.collection.insert_one(data) - inserts one document
    total = self.collection.count_documents({}) - Counts the total documents within the database
    results = list(self.collection.find(query)) - quick look up for existing documents

## Read - 
This gives the user the ability to read the pre existing documentation within the Mongo DB database

  results = list(self.collection.find(query)) - MongoDB query so one may read the documents

## Update - preexisting documentation inside the database can be edited using the follwing commands...
    updateOne = list(self.collection.updateOne()) - Updates a single document
    updateMany = list(self.collection.updateMany()) - Updates multiple documents
    replaceOne = list(self.collection.replaceOne()) - Replaces one document of the user's choice
    replaceOne = list(self.collection.replaceMany()) - Replaces multiple documents of the user's choice
  queryCount = query - Counts how many queries are within the database curently

## Delete - 
The last bit of functionality in the code for users is not delete any information that may not be needed... or, If one makes a mistake when inserting queries

   deleteOne = list(self.collection.deleteOne())
deleteMany = list(seld.collection.deleteMany())
        

## Resources
CS 340 Jupyter Notebook in Apporto (Virtual Lab) Tutorial PDF
CS 340 Dashboard Specifications Document PDF
CS 340 Mongo in Apporto (Virtual Lab) Tutorial PDF
Headfirst Python

