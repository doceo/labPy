#for loop
#Dictionaries
#keys
#finding letter "r" in our dictionary keys

students={
    "male":["Tom","Charlie","Oscar","Frank"],
    "female":["Sarah","Huda","Samantha","Emily"]
    }
for key in students.keys():
    #print(key)
    for name in students[key]:
        if "r" in name:
            print(name)
            

