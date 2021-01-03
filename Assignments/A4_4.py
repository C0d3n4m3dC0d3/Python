#4. Write a python script to check whether a given key already exists in a
#dictionary

stationery = {
              "P1" : {
                        "Name" : "Pen",
                        "Price" : 10.0, 
                        "Stock" : 50,
                        "Brand" : "Pinpoint"
                        },
              "P2" : {
                        "Name" : "Notebook",
                        "Price" : 40.0,
                        "Stock" : 20,
                        "Brand" : "Classmates"
                        },
              "P3" : {
                        "Name" : "Correction Tape",
                        "Price" : 25.0,
                        "Stock" : 80,
                        "Brand" : "Camlin Kokuyo"
                        }
          } 

key = input("Enter key: ")
if key in stationery.keys():
    print("Key exists!")
else:
    print("Key does not exist!")
