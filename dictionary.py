myDictionary = {"name1" : "Parker", "name2" : "Jim", "name3" : "Joe"}
print(myDictionary)
myDictionary.update({"name4" : "Jemi", "name5" : "Jill"})
print(myDictionary)
del myDictionary["name4"]
print(myDictionary)
myDictionary["name5"] = "Jack"
print(myDictionary)

fullname = input("Please enter your full name: ")
myDictionary.update({"name6" : fullname})
print(myDictionary)