from threading import Thread
from DataLibrary import Data
print("1.Enter the directory where you want to store your JSON file\n")
print("2.Store file in Current directory\n")
n=int(input("Enter the number: "))
if n==2:
    a=Data()
    key=input("Enter the Key: ")
    value=int(input("Enter the value: "))
    t1=Thread(target=a.create(key,value))
    t2=Thread(target=a.read(key))
    t3=Thread(target=a.delete(key))
    t1.start()#Thread 1 starts
    t1.join()#Thread 1 ends and waits for next thread to start
    t2.start()#Thread 2 starts
    t2.join()#Thread 2 ends and waits for next thread to start
    t3.start()#Thread 3 starts
    t3.join()#Thread 3 ends and waits for next thread to start
    print("Process completed!")  
else:
    d=input("Enter the directory")
    a=Data(d)
    key=input("Enter the Key: ")
    value=int(input("Enter the value: "))
    t1=Thread(target=a.create(key,value))
    t2=Thread(target=a.read(key))
    t3=Thread(target=a.delete(key))
    t1.start()#Thread 1 starts
    t1.join()#Thread 1 ends and waits for next thread to start
    t2.start()#Thread 2 starts
    t2.join()#Thread 2 ends and waits for next thread to start
    t3.start()#Thread 3 starts
    t3.join()#Thread 3 ends and waits for next thread to start
    print("Process completed!")
    
