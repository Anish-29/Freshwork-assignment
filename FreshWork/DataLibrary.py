import time
import json
from os import path,getcwd

data={} #data will be stored in dictionary  
class Data:
    def __init__(self,cdir=getcwd()): #getcwd is used to get the current working directory
        self.filo=cdir
        if(path.isdir(self.filo)): #checks wheather the location exists
            try:
                self.filename='\\'+input("Enter the file name : ")+".json" #Name of the json file created
                f = open(str(self.filo)+self.filename,"x")
                f.write(json.dumps(data))
                
            except:
                print("Error : File name already exist .")
        else:
            print("Error : File directory does not exist")
    def create(self,key,value,t=0):
        if key in data:
            print("Error : Key already exists") #checks for key existance in dictionary
        else:
            if key.isalpha():
                if len(data) <(1024**3) and value<=(16*1024*1024): #constraints for file size less than 1GB and Jasonobject value less than 16KB 
                    if(len(key)>32): #constrints for key capped at 32 characters
                        print("Error : The key should not exceed 32 characters")
                    else:
                        entry_time=t
                        if t!=0:
                            entry_time=int(time.time())+t
                        data[key]=[value,entry_time]
                        json_data = json.dumps(data) #converts the dictionary to Json 
                        with open(str(self.filo)+self.filename,"w") as f:
                            f.write(json_data) #writing the file
                        print("Success : Data is successfully created!")
                else:

                    print("Error : Memory limit reached")
            else:
                print("Error : Please enter a key with alphabets only")
    def read(self,key):
        if key in data:
            values=data[key]
            if values[1] < int(time.time()) and values[1]!=0: #checks the time-to-live property
                print("Error : Time-to-live for the key is expired")
            else:
                print("key :"+str(key)+",\n"+"Value :"+str(values[0]))#for returning the JSON format
        else:
            print("Error : Key does not exist")
            
    def delete(self,key):
        if key in data:
            values=data[key]
            if values[1] < int(time.time()) and values[1]!=0:
                print("Error : Time-to-live for the key is expired")
            else:
                del data[key]
                print("Success : The key has been deleted!")
        else:
            print("Error : Key does not exist")
   


    
